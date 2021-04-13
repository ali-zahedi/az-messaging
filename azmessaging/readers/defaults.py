from azmessaging import default_settings as settings
from azmessaging.utils import get_continent, import_class
from .bases import Reader
from ..sms import SMSApi


class DefaultReader(Reader):

    def read(self, channel: str, identifier: str) -> dict:
        """

        :param channel:
        :param identifier:
        :return:
        base on channel type for example for sms:
        'SMS': {
            'SNS': {
                'ACCESS_KEY_ID': os.environ.get('SNS_ACCESS_KEY_ID', None),
                'SECRET_ACCESS_KEY': os.environ.get('SNS_SECRET_ACCESS_KEY', None),
            },
            'TWILIO': {
                'ACCOUNT_SID': os.environ.get('TWILIO_ACCOUNT_SID', None),
                'AUTH_TOKEN': os.environ.get('TWILIO_AUTH_TOKEN', None),
                'SENDER': os.environ.get('TWILIO_SENDER', None),
            }
        }
        """
        return getattr(settings, 'MESSAGING', {}).get(channel, {})

    def get_sms_sender(self, identifier: str, country_code: str) -> SMSApi:
        continent = get_continent(country_code).upper()
        for sp_name in settings.SMS_CONFIG['PRIORITY_SERVICE_PROVIDER']:
            kwargs = self._sms_config_reader(sp_name)
            sp = settings.SMS_CONFIG['SERVICE_PROVIDER'][sp_name]
            for r in sp['ROUTING']:
                if continent in r['continents'] or country_code in r['countries']:
                    r_copy = r.copy()
                    del r_copy['continents']
                    del r_copy['countries']
                    kwargs.update(r_copy)
                    klass = import_class(sp['CLASS'])
                    return klass(**kwargs)

        # Default
        sp_name = settings.SMS_CONFIG['DEFAULT_SERVICE_PROVIDER']
        sp = settings.SMS_CONFIG['SERVICE_PROVIDER'][sp_name]
        kwargs = self._sms_config_reader(sp_name)
        klass = import_class(sp['CLASS'])
        return klass(**kwargs)

    @classmethod
    def _sms_config_reader(cls, service_provider_name):
        kwargs = {}
        sp = settings.SMS_CONFIG['SERVICE_PROVIDER'][service_provider_name]
        kwargs.update(sp)
        del kwargs['ROUTING']
        del kwargs['CLASS']
        return kwargs
