import abc

from azmessaging import default_settings as settings
from azmessaging.readers.pushnotifications import PushNotificationConfig
from azmessaging.utils import import_class


class PushNotificationReaderMixin:

    @abc.abstractmethod
    def get_push_notification_config_class(self) -> type(PushNotificationConfig):
        pass

    @abc.abstractmethod
    def get_push_notification_config(self, identifier) -> PushNotificationConfig:
        pass

    def get_push_notification_sender_class(self, service_provider_name):
        settings.PUSH_NOTIFICATION_CONFIG['SERVICE_PROVIDER_CLASS'].get(service_provider_name, None)
        class_path = self.get_push_notification_config_class().get_service_provider_class_path(service_provider_name)
        klass = import_class(class_path)
        return klass

    def get_push_notification_sender(self, identifier: str) -> str:
        config = self.get_push_notification_config(identifier)
        for tp_name in config.priorities_service_provider:
            kwargs = self._push_notification_constructor_parameter(config, tp_name)
            klass = self.get_push_notification_sender_class(tp_name)
            return klass(**kwargs)
        # Default
        tp_name = config.default_service_provider
        sp = config.service_providers[tp_name]
        kwargs = self._push_notification_constructor_parameter(config, tp_name)
        klass = self.get_push_notification_sender_class(tp_name)
        return klass(**kwargs)

    @classmethod
    def _push_notification_constructor_parameter(cls, config, service_provider_name) -> dict:
        kwargs = {}
        sp = config.service_providers[service_provider_name]
        kwargs.update(sp)
        del kwargs['CLASS']
        return kwargs
