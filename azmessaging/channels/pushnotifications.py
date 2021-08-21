from .base import BaseNotificationChannel


class PushNotificationChannel(BaseNotificationChannel):
    """
    structure: []
    for example:
    ["token_1", "token_2", "token_3", ]
    """
    _receivers = []

    def __init__(self, data, **kwargs):
        super(PushNotificationChannel, self).__init__(**kwargs)
        self.data = data

    def _send_msg(self, message, receivers, data):
        sender = self.reader.get_push_notification_sender(self.identifier)
        sender.bulk_send(receivers, message, data)

    def get_message(self):
        return self.raw_message

    def set_receivers(self, receivers: list):
        self._receivers = receivers

    def get_receivers(self):
        return self._receivers

    def notify(self):
        """Sends the notification."""
        self._send_msg(message=self.get_message(), receivers=self.get_receivers(), data=self.data)
