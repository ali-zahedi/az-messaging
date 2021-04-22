import abc

import six

from azmessaging import default_settings as settings
from azmessaging.readers.smsconfig import SMSConfig
from azmessaging.utils import import_class, get_continent


@six.add_metaclass(abc.ABCMeta)
class Reader:

    @abc.abstractmethod
    def get_sms_config_class(self) -> type(SMSConfig):
        pass

    @abc.abstractmethod
    def get_sms_config(self, identifier) -> SMSConfig:
        pass

    def klass(self, channel: str, identifier: str) -> dict:
        return import_class(settings.CHANNEL_CLASS[channel.upper()])

    def get_sms_sender_class(self, service_provider_name):
        class_path = self.get_sms_config_class().get_service_provider_class_path(service_provider_name)
        klass = import_class(class_path)
        return klass

    def get_sms_sender(self, identifier: str, country_code: str) -> str:
        config = self.get_sms_config(identifier)
        continent = get_continent(country_code).upper()
        for sp_name in config.priorities_service_provider:
            sp = config.service_providers[sp_name]
            for r in sp['ROUTING']:
                if continent in r['continents'] or country_code in r['countries']:
                    kwargs = self._sms_constructor_parameter(config, sp_name)
                    r_copy = r.copy()
                    del r_copy['continents']
                    del r_copy['countries']
                    kwargs.update(r_copy)
                    klass = self.get_sms_sender_class(sp_name)
                    return klass(**kwargs)

        # Default
        sp_name = config.default_service_provider
        sp = config.service_providers[sp_name]
        kwargs = self._sms_constructor_parameter(config, sp_name)
        klass = self.get_sms_sender_class(sp_name)
        return klass(**kwargs)

    @classmethod
    def _sms_constructor_parameter(cls, config, service_provider_name) -> dict:
        kwargs = {}
        sp = config.service_providers[service_provider_name]
        kwargs.update(sp)
        del kwargs['ROUTING']
        del kwargs['CLASS']
        return kwargs
