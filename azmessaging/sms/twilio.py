from twilio.rest import Client

from .smsabstract import SMSApi
from ..models import SMSNotificationType


class SMSAPITwilio(SMSApi):

    def __init__(self, account_sid, auth_token, sender, **kwargs):
        super(SMSAPITwilio, self).__init__(**kwargs)
        self.api = Client(
            account_sid,
            auth_token,
        )
        self._sender = sender

    def bulk_send(self, phone_numbers: [str], message: str, sms_type: SMSNotificationType):
        # TODO: handle bulk options
        for phone_number in phone_numbers:
            self.send(phone_number, message, sms_type)

    def send(self, phone_number: str, message: str, sms_type: SMSNotificationType):
        response = self.api.messages.create(
            body=message,
            from_=self._sender,
            to=phone_number
        )
        # TODO: handle response

