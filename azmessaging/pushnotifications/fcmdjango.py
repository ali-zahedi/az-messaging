import fcm_django

if fcm_django.__version__ >= '1.0.0':
    raise ImportError('FCMDjango version must be lower than version 1.')

from fcm_django.models import FCMDevice

from .pushabstract import PushNotificationAPI


class FCMDjangoAPI(PushNotificationAPI):

    def __init__(self, api_key, **kwargs):
        super(FCMDjangoAPI, self).__init__(**kwargs)
        self.api_key = api_key

    def bulk_send(self, title: str, message: str, image_url: str, receivers: list,
                  payload_data: dict):
        try:
            fcm_devices = FCMDevice.objects.filter(
                active=True,
                registration_id__in=receivers,
            ).distinct()
            sent_result = fcm_devices.send_message(
                title=title,
                body=message,
                icon=image_url,
                data=payload_data,
                api_key=self.api_key,
            )
            # TODO: handle response to log and etc...
        except Exception as inst:
            # obj.description_for_admin = 'type: {0}\nargs: {1}\ninstance: {2}'.format(type(inst), inst.args, inst)
            # obj.save()
            # TODO: handle response to log and etc...
            pass

    def send(self, title: str, message: str, image_url: str, receiver: str, payload_data: dict):
        self.bulk_send(title, message, image_url, [receiver], payload_data)
