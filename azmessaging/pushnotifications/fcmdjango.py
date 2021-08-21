import fcm_django

if fcm_django.__version__ >= '1.0.0':
    raise ImportError('FCMDjango version must be lower than version 1.')

from fcm_django.models import FCMDevice

from .pushabstract import PushNotificationAPI


class FCMDjangoAPI(PushNotificationAPI):

    def __init__(self, api_key, **kwargs):
        super(FCMDjangoAPI, self).__init__(**kwargs)
        self.api_key = api_key

    def bulk_send(self, title: str, body: str, image_url: str, tokens: list, extra_data: dict, payload_data: dict):
        try:
            fcm_devices = FCMDevice.objects.filter(
                registration_id__in=tokens,
            ).distinct()
            sent_result = fcm_devices.send_message(
                title=title,
                body=body,
                icon=image_url,
                api_key=self.api_key,
            )
            # TODO: handle response to log and etc...
        except Exception as inst:
            # obj.description_for_admin = 'type: {0}\nargs: {1}\ninstance: {2}'.format(type(inst), inst.args, inst)
            # obj.save()
            # TODO: handle response to log and etc...
            pass

    def send(self, title: str, body: str, image_url: str, token: str, extra_data: dict, payload_data: dict):
        self.bulk_send(title, body, image_url, [token], extra_data, payload_data)
