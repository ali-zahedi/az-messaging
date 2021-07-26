import abc
import six


@six.add_metaclass(abc.ABCMeta)
class TelegramApi:

    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def send(self, username: str, message: str):
        pass

    @abc.abstractmethod
    def bulk_send(self, usernames: [str], message: str):
        pass
