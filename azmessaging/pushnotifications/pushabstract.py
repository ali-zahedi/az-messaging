import abc
import six


@six.add_metaclass(abc.ABCMeta)
class PushNotificationAPI:

    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def send(self, title: str, body: str, image_url: str, token: str, extra_data: dict, payload_data: dict):
        """

        :param title:
        :param body:
        :param image_url:
        :param token:
        :param extra_data: use for main body of notification
        :param payload_data: use for data in push notification
        :return:
        """
        pass

    @abc.abstractmethod
    def bulk_send(self, title: str, body: str, image_url: str, tokens: list, extra_data: dict, payload_data: dict):
        """

        :param title:
        :param body:
        :param image_url:
        :param tokens:
        :param extra_data: use for main body of notification
        :param payload_data: use for data in push notification
        :return:
        """
        pass
