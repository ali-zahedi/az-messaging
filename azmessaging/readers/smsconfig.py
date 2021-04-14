class SMSConfig:
    def __init__(self, default, priorities, service_providers):
        self.default_service_provider = default
        self.priorities_service_provider = priorities
        self.service_providers = service_providers

    default_service_provider: str
    priorities_service_provider: [str]
    service_providers: dict
