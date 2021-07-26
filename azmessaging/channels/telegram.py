from .base import BaseNotificationChannel


class TelegramNotificationChannel(BaseNotificationChannel):
    """
    structure: []
    for example:
    ["user_1", "user_2", "user_3", ]
    """
    _receivers = []

    def __init__(self, **kwargs):
        super(TelegramNotificationChannel, self).__init__(**kwargs)

    def _send_msg(self, message, users):
        sender = self.reader.get_telegram_sender(self.identifier)
        sender.bulk_send(users, message)

    def get_message(self):
        return self.raw_message

    def set_receivers(self, users: list):
        self._receivers = users

    def get_receivers(self):
        return self._receivers

    def notify(self):
        """Sends the notification."""
        self._send_msg(message=self.get_message(), users=self.get_receivers())
