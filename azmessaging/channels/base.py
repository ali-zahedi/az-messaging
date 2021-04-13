import abc

import six
from azmessaging import default_settings as settings


@six.add_metaclass(abc.ABCMeta)
class BaseNotificationChannel:
    identifier = None
    """Base channel for sending notifications."""

    def __init__(self, identifier: str, message: str, **kwargs):
        self.identifier = identifier
        self.raw_message = message
        self.reader = settings.READER

    @abc.abstractmethod
    def get_message(self):
        """get message."""
        pass

    @abc.abstractmethod
    def notify(self):
        """Sends the notification."""
        pass
