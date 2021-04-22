from azmessaging import default_settings as settings
from .bases import Reader
from .smsconfig import SMSConfig


class DefaultReader(Reader):

    def get_sms_config_class(self) -> type(SMSConfig):
        return SMSConfig

    def get_sms_config(self, identifier) -> SMSConfig:
        return SMSConfig(
            default=settings.SMS_CONFIG['DEFAULT_SERVICE_PROVIDER'],
            priorities=settings.SMS_CONFIG['PRIORITY_SERVICE_PROVIDER'],
            service_providers=settings.SMS_CONFIG['SERVICE_PROVIDER'],
            white_list_countries=settings.SMS_CONFIG['WHITE_LIST'],
            black_list_countries=settings.SMS_CONFIG['BLACK_LIST'],
        )
