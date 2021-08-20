from .telegramabstract import TelegramApi


class TELEGRAMAPIDefaultAPI(TelegramApi):

    def __init__(self, api_key, api_server, **kwargs):
        super(TELEGRAMAPIDefaultAPI, self).__init__(**kwargs)
        self.api_key = api_key
        self.api_server = api_server

    def bulk_send(self, usernames: [str], message: str):
        # TODO: handle bulk options
        for username in usernames:
            self.send(username, message)

    def send(self, username: str, message: str):
        # TODO: handle send by your self
        raise NotImplementedError("You must Implement by your self to send to telegram")
