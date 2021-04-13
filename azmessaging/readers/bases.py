import abc

import pytz
import six

from azmessaging import default_settings as settings
from azmessaging.sms import SMSApi


@six.add_metaclass(abc.ABCMeta)
class Reader:

    @abc.abstractmethod
    def read(self, channel: str, identifier: str) -> dict:
        """

        :param channel:
        :param identifier:
        :return:
        base on channel type for example for sms:
        'SMS': {
            'SNS': {
                'ACCESS_KEY_ID': os.environ.get('SNS_ACCESS_KEY_ID', None),
                'SECRET_ACCESS_KEY': os.environ.get('SNS_SECRET_ACCESS_KEY', None),
            },
            'TWILIO': {
                'ACCOUNT_SID': os.environ.get('TWILIO_ACCOUNT_SID', None),
                'AUTH_TOKEN': os.environ.get('TWILIO_AUTH_TOKEN', None),
                'SENDER': os.environ.get('TWILIO_SENDER', None),
            }
        }
        """
        pass

    def klass(self, channel: str, identifier: str) -> dict:
        return settings.CHANNEL_CLASS[channel.upper()]

    @abc.abstractmethod
    def get_sms_sender(self, identifier: str, country_code: str) -> SMSApi:
        pass
