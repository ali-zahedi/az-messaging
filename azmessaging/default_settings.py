"""Default settings for messaging."""

import django
from django.conf import settings

from .exceptions import AZSettingDoesNotExist

if django.__version__ >= '3.0':
    from django.db import models

    TEXT_CHOICES = models.TextChoices
else:
    from .models.enum_django import TextChoices

    TEXT_CHOICES = TextChoices

MESSAGING = getattr(settings, 'AZ_MESSAGING', {})

SETTING_VALUE_READER_CLASS = MESSAGING.get('SETTING_VALUE_READER_CLASS', 'azmessaging.readers.DefaultReader')

CHANNEL_CLASS = MESSAGING.get(
    'CLASS',
    {
        'SMS': 'azmessaging.channels.SMSNotificationChannel',
        'TELEGRAM': 'azmessaging.channels.TelegramNotificationChannel',
    }
)

"""
READER
Load in app config after application loaded
"""
READER = None

"""
SMS
"""
SMS_CONFIG = MESSAGING.get('SMS', {})
if len(SMS_CONFIG) != 0:
    SMS_CONFIG['WHITE_LIST'] = SMS_CONFIG.get('WHITE_LIST', '__all__')
    SMS_CONFIG['BLACK_LIST'] = SMS_CONFIG.get('BLACK_LIST', '__none__')
    if not SMS_CONFIG.get('DEFAULT_SERVICE_PROVIDER', None) or \
            len(SMS_CONFIG.get('SERVICE_PROVIDER', {}).get(SMS_CONFIG['DEFAULT_SERVICE_PROVIDER'], {})) == 0:
        raise AZSettingDoesNotExist('SMS configuration: please check `DEFAULT_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    if len(SMS_CONFIG.get('PRIORITY_SERVICE_PROVIDER', [])) == 0 or \
            len(list(filter(lambda x: SMS_CONFIG['SERVICE_PROVIDER'].get(x),
                            SMS_CONFIG['PRIORITY_SERVICE_PROVIDER']))) != len(SMS_CONFIG['PRIORITY_SERVICE_PROVIDER']):
        raise AZSettingDoesNotExist(
            'SMS configuration: please check `PRIORITY_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    sp_class = {}
    for sp_name in SMS_CONFIG['SERVICE_PROVIDER']:
        sp = SMS_CONFIG['SERVICE_PROVIDER'][sp_name]
        if not sp.get('CLASS', None):
            raise AZSettingDoesNotExist(
                f'SMS configuration: please add `CLASS` on `{sp_name}`')
        sp_class[sp_name] = sp.get('CLASS')
        for r in sp.get('ROUTING', []):
            r['countries'] = list(filter(None, [x.strip().upper() for x in r.get('countries', '').split(',')]))
            r['continents'] = list(filter(None, [x.strip().upper() for x in r.get('continents', '').split(',')]))
    SMS_CONFIG['SERVICE_PROVIDER_CLASS'] = sp_class

"""
TELEGRAM
"""
TELEGRAM_CONFIG = MESSAGING.get('TELEGRAM', {})
if len(TELEGRAM_CONFIG) != 0:
    if not TELEGRAM_CONFIG.get('DEFAULT_SERVICE_PROVIDER', None) or \
            len(TELEGRAM_CONFIG.get('SERVICE_PROVIDER', {}).get(TELEGRAM_CONFIG['DEFAULT_SERVICE_PROVIDER'], {})) == 0:
        raise AZSettingDoesNotExist('Telegram configuration: please check `DEFAULT_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    if len(TELEGRAM_CONFIG.get('PRIORITY_SERVICE_PROVIDER', [])) == 0 or \
            len(list(filter(lambda x: TELEGRAM_CONFIG['SERVICE_PROVIDER'].get(x),
                            TELEGRAM_CONFIG['PRIORITY_SERVICE_PROVIDER']))) != len(TELEGRAM_CONFIG['PRIORITY_SERVICE_PROVIDER']):
        raise AZSettingDoesNotExist(
            'Telegram configuration: please check `PRIORITY_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    tp_class = {}
    for tp_name in TELEGRAM_CONFIG['SERVICE_PROVIDER']:
        tp = TELEGRAM_CONFIG['SERVICE_PROVIDER'][tp_name]
        if not tp.get('CLASS', None):
            raise AZSettingDoesNotExist(
                f'Telegram configuration: please add `CLASS` on `{tp_name}`')
        tp_class[tp_name] = tp.get('CLASS')
    TELEGRAM_CONFIG['SERVICE_PROVIDER_CLASS'] = tp_class
