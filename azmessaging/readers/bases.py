import abc

import six

from azmessaging import default_settings as settings
from azmessaging.utils import import_class


@six.add_metaclass(abc.ABCMeta)
class Reader:

    def klass(self, channel: str, identifier: str) -> dict:
        return import_class(settings.CHANNEL_CLASS[channel.upper()])
