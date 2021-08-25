from azmessaging import default_settings as settings
from .bases import Reader
from .sms import SMSReaderMixin, SMSConfig
from .telegram import TelegramReaderMixin, TelegramConfig
from .pushnotifications import PushNotificationReaderMixin, PushNotificationConfig


class DefaultReader(Reader, SMSReaderMixin, TelegramReaderMixin, PushNotificationReaderMixin):

    def get_push_notification_config_class(self) -> type(PushNotificationConfig):
        return PushNotificationConfig

    def get_push_notification_config(self, identifier) -> PushNotificationConfig:
        return self.get_push_notification_config_class()(
            default=settings.PUSH_NOTIFICATION_CONFIG['DEFAULT_SERVICE_PROVIDER'],
            priorities=settings.PUSH_NOTIFICATION_CONFIG['PRIORITY_SERVICE_PROVIDER'],
            service_providers=settings.PUSH_NOTIFICATION_CONFIG['SERVICE_PROVIDER'],
        )

    def get_telegram_config(self, identifier) -> TelegramConfig:
        return self.get_telegram_config_class()(
            default=settings.TELEGRAM_CONFIG['DEFAULT_SERVICE_PROVIDER'],
            priorities=settings.TELEGRAM_CONFIG['PRIORITY_SERVICE_PROVIDER'],
            service_providers=settings.TELEGRAM_CONFIG['SERVICE_PROVIDER'],
        )

    def get_telegram_config_class(self) -> type(TelegramConfig):
        return TelegramConfig

    def get_sms_config_class(self) -> type(SMSConfig):
        return SMSConfig

    def get_sms_config(self, identifier) -> SMSConfig:
        return self.get_sms_config_class()(
            default=settings.SMS_CONFIG['DEFAULT_SERVICE_PROVIDER'],
            priorities=settings.SMS_CONFIG['PRIORITY_SERVICE_PROVIDER'],
            service_providers=settings.SMS_CONFIG['SERVICE_PROVIDER'],
            white_list_countries=settings.SMS_CONFIG['WHITE_LIST'],
            black_list_countries=settings.SMS_CONFIG['BLACK_LIST'],
        )
