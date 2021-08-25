import abc
import six


@six.add_metaclass(abc.ABCMeta)
class PushNotificationAPI:

    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def send(self, title: str, message: str, image_url: str, receiver: str, payload_data: dict):
        """

        :param title:
        :param message:
        :param image_url:
        :param receiver:
        :param payload_data: use for data in push notification
        :return:
        """
        pass

    @abc.abstractmethod
    def bulk_send(self, title: str, message: str, image_url: str, receivers: list, payload_data: dict):
        """

        :param title:
        :param message:
        :param image_url:
        :param receivers:
        :param payload_data: use for data in push notification
        :return:
        """
        pass
