"""Default settings for messaging."""

from django.conf import settings
import django

from .exceptions import AZSettingDoesNotExist

if django.__version__ >= '3.0':
    from django.db import models

    TEXT_CHOICES = models.TextChoices
else:
    from .models.enum_django import TextChoices

    TEXT_CHOICES = TextChoices

MESSAGING = getattr(settings, 'AZ_MESSAGING', {})

SETTING_VALUE_READER_CLASS = getattr(MESSAGING, 'SETTING_VALUE_READER_CLASS', 'azmessaging.readers.DefaultReader')

CHANNEL_CLASS = getattr(
    MESSAGING,
    'CLASS',
    {
        'SMS': 'azmessaging.channels.SMSNotificationChannel',
    }
)
"""
SMS
"""
SMS_CONFIG = MESSAGING.get('SMS', {})
if len(SMS_CONFIG) != 0:
    if not SMS_CONFIG.get('DEFAULT_SERVICE_PROVIDER', None) or \
            len(SMS_CONFIG.get('SERVICE_PROVIDER', {}).get(SMS_CONFIG['DEFAULT_SERVICE_PROVIDER'], {})) == 0:
        raise AZSettingDoesNotExist('SMS configuration: please check `DEFAULT_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    if len(SMS_CONFIG.get('PRIORITY_SERVICE_PROVIDER', [])) == 0 or \
            len(list(filter(lambda x: SMS_CONFIG['SERVICE_PROVIDER'].get(x),
                            SMS_CONFIG['PRIORITY_SERVICE_PROVIDER']))) != len(SMS_CONFIG['PRIORITY_SERVICE_PROVIDER']):
        raise AZSettingDoesNotExist(
            'SMS configuration: please check `PRIORITY_SERVICE_PROVIDER` and `SERVICE_PROVIDER`')

    for sp_name in SMS_CONFIG['SERVICE_PROVIDER']:
        sp = SMS_CONFIG['SERVICE_PROVIDER'][sp_name]
        if not sp.get('CLASS', None):
            raise AZSettingDoesNotExist(
                f'SMS configuration: please add `CLASS` on `{sp_name}`')

        for r in sp.get('ROUTING', []):
            r['countries'] = list(filter(None, [x.strip().upper() for x in r.get('countries', '').split(',')]))
            r['continents'] = list(filter(None, [x.strip().upper() for x in r.get('continents', '').split(',')]))
