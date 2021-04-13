import abc
import six
from azmessaging.models import SMSNotificationType

@six.add_metaclass(abc.ABCMeta)
class SMSApi:

    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def send(self, phone_number: str, message: str, sms_type: SMSNotificationType):
        pass

    @abc.abstractmethod
    def bulk_send(self, phone_numbers: [str], message: str, sms_type: SMSNotificationType):
        pass
