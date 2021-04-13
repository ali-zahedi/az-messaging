import boto3

from .smsabstract import SMSApi
from ..models import SMSNotificationType


class SMSAPISNSAmazon(SMSApi):

    def __init__(self, key_id, access_key, region_name, **kwargs):
        super(SMSAPISNSAmazon, self).__init__(**kwargs)
        self.api = boto3.client(
            'sns',
            aws_access_key_id=key_id,
            aws_secret_access_key=access_key,
            region_name=region_name,
        )

    def bulk_send(self, phone_numbers: [str], message: str, sms_type: SMSNotificationType):
        # TODO: handle bulk options
        for phone_number in phone_numbers:
            self.send(phone_number, message, sms_type)

    def send(self, phone_number: str, message: str, sms_type: SMSNotificationType):
        sms_type_string = 'Promotional' if sms_type == SMSNotificationType.PROMOTIONAL else 'Transactional'
        response = self.api.publish(
            PhoneNumber=phone_number,
            Message=message,
            MessageAttributes={
                'AWS.SNS.SMS.SMSType': {
                    'DataType': 'String',
                    'StringValue': sms_type_string
                }
            }
        )
        # TODO: handle response
