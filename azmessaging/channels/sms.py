from phonenumbers import region_code_for_country_code, parse as phone_number_parse
from azmessaging.models import SMSNotificationType
from .base import BaseNotificationChannel


class SMSNotificationChannel(BaseNotificationChannel):
    """
    structure: {"country_code": []}
    for example:
    {"US": ["+15124467"], "UK": []}
    """
    _receivers = {}
    sms_type = SMSNotificationType.PROMOTIONAL

    def __init__(self, sms_type, **kwargs):
        super(SMSNotificationChannel, self).__init__(**kwargs)
        self.sms_type = sms_type

    def _send_msg(self, message, phone_numbers, country_code):
        sender = self.reader.get_sms_sender(self.identifier, country_code=country_code)
        sender.bulk_send(phone_numbers, message, self.sms_type)

    def set_receivers(self, phone_numbers: list):
        self._receivers = {}
        config = self.reader.get_sms_config(self.identifier)
        for item in phone_numbers:
            country_code = region_code_for_country_code(phone_number_parse(item).country_code)
            if country_code not in config.white_list_countries:
                continue
            if country_code not in self._receivers:
                self._receivers[country_code] = set()
            self._receivers[country_code].add(item)

    def get_receivers(self):
        return self._receivers

    def get_message(self):
        return self.raw_message

    def notify(self):
        """Sends the notification."""
        for country_code in self.get_receivers():
            self._send_msg(self.get_message(), phone_numbers=self.get_receivers()[country_code],
                           country_code=country_code)
