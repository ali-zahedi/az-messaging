from .base import BaseNotificationChannel


class PushNotificationChannel(BaseNotificationChannel):
    """
    structure: []
    for example:
    ["token_1", "token_2", "token_3", ]
    """
    _receivers = []

    def __init__(self, title, image_url, payload_data, **kwargs):
        super(PushNotificationChannel, self).__init__(**kwargs)
        self.title = title
        self.image_url = image_url
        self.payload_data = payload_data

    def _send_msg(self, title, message, image_url, receivers, payload_data):
        sender = self.reader.get_push_notification_sender(self.identifier)
        sender.bulk_send(
            title=title,
            message=message,
            image_url=image_url,
            receivers=receivers,
            payload_data=payload_data,
        )

    def get_message(self):
        return self.raw_message

    def set_receivers(self, receivers: list):
        self._receivers = receivers

    def get_receivers(self):
        return self._receivers

    def notify(self):
        """Sends the notification."""
        self._send_msg(
            title=self.title,
            message=self.get_message(),
            image_url=self.image_url,
            receivers=self.get_receivers(),
            payload_data=self.payload_data
        )
