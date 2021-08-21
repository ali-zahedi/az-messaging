from azmessaging import default_settings as settings


class PushNotificationConfig:
    default_service_provider: str
    priorities_service_provider: [str]
    service_providers: dict

    def __init__(self, default, priorities, service_providers):
        self.default_service_provider = default
        self.priorities_service_provider = priorities
        self.service_providers = service_providers

    @classmethod
    def get_service_provider_class_path(cls, service_provider_name) -> str:
        return settings.PUSH_NOTIFICATION_CONFIG['SERVICE_PROVIDER_CLASS'].get(service_provider_name, None)
