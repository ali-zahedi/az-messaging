import pytz


class SMSConfig:
    _service_provider_class_path: dict
    default_service_provider: str
    priorities_service_provider: [str]
    service_providers: dict
    white_list_countries: [str]

    def __init__(self, default, priorities, service_providers, white_list_countries, black_list_countries):
        self.default_service_provider = default
        self.priorities_service_provider = priorities
        self.service_providers = service_providers
        """
        white list
        """
        if white_list_countries == '__all__':
            wlc = set(pytz.country_names)
        elif white_list_countries == '__none__' or not white_list_countries:
            wlc = set()
        else:
            wlc = set(filter(None, [x.strip().upper() for x in white_list_countries.split(',')]))
        """
        black list
        """
        if black_list_countries == '__all__':
            blc = set(pytz.country_names)
        elif black_list_countries == '__none__' or not black_list_countries:
            blc = set()
        else:
            blc = set(filter(None, [x.strip().upper() for x in black_list_countries.split(',')]))

        self.white_list_countries = wlc - blc

    @classmethod
    def get_service_provider_class_path(cls, service_provider_name) -> str:
        return cls._service_provider_class_path.get(service_provider_name, None)

    @classmethod
    def set_service_provider_class_path(cls, service_providers_class_path):
        cls._service_provider_class_path = service_providers_class_path
