<!--![GitHub All Releases](https://img.shields.io/github/downloads/ali-zahedi/az-messaging/total)-->
<!--![GitHub issues](https://img.shields.io/github/issues/ali-zahedi/az-messaging)-->
![GitHub](https://img.shields.io/github/license/ali-zahedi/az-messaging)
![GitHub](https://img.shields.io/pypi/pyversions/az-messaging.svg?maxAge=2592000)
![GitHub](https://img.shields.io/pypi/v/az-messaging.svg?maxAge=2592000)
# AZ Messaging config

[[_TOC_]]

## Install with `pip`

```shell script
pip install az-messaging
```

### settings.py

 
 ``` python
INSTALLED_APPS = [
    # ....
    'azmessaging',
    # ...
]

AZ_MESSAGING = {
    'SETTING_VALUE_READER_CLASS': 'azmessaging.readers.DefaultReader',
    'CLASS': {
        'SMS': 'azmessaging.channels.SMSNotificationChannel',
        'TELEGRAM': 'azmessaging.channels.TelegramNotificationChannel',
    },
    'TELEGRAM': {
        'SERVICE_PROVIDER': {
            'DEFAULT': {
                'CLASS': 'azmessaging.telegram.TELEGRAMAPIDefaultAPI',
                'api_key': os.environ.get('TELEGRAM_DEFAULT_API_KEY', None),
                'api_server': os.environ.get('TELEGRAM_DEFAULT_API_SERVER', None),
            },
        },
        'DEFAULT_SERVICE_PROVIDER': 'DEFAULT',  # REQUIRED
        'PRIORITY_SERVICE_PROVIDER': [  # REQUIRED
            'DEFAULT',
        ],
    },
    'SMS': {
        'SERVICE_PROVIDER': {
            'SNS': {
                'CLASS': 'azmessaging.sms.SMSAPISNSAmazon',
                'ROUTING': [
                    {
                        'countries': 'UK, US',
                        'region_name': 'eu-west-1'
                    },
                    {
                        'continents': 'EUROPE, AFRICA',
                        'region_name': 'eu-west-2'
                    }
                ],
                'key_id': os.environ.get('AWS_ACCESS_KEY_ID', None),
                'access_key': os.environ.get('AWS_SECRET_ACCESS_KEY', None),
                'region_name': os.environ.get('AWS_SNS_DEFAULT_REGION', None),
            },
            'TWILIO': {
                'CLASS': 'azmessaging.sms.SMSAPITwilio',
                'ROUTING': [
                    {
                        'countries': 'DE, EE',
                        'sender': os.environ.get('TWILIO_EE_SENDER', None),
                    },
                    {
                        'continents': 'ASIA',
                        'sender': os.environ.get('TWILIO_ASIA_SENDER', None),
                    }
                ],
                'account_sid': os.environ.get('TWILIO_ACCOUNT_SID', None),
                'auth_token': os.environ.get('TWILIO_AUTH_TOKEN', None),
                'sender': os.environ.get('TWILIO_DEFAULT_SENDER', None),
            },
        },
        'DEFAULT_SERVICE_PROVIDER': 'SNS',  # REQUIRED
        'PRIORITY_SERVICE_PROVIDER': [      # REQUIRED
            'TWILIO',
            'SNS',
        ],
        'WHITE_LIST': '__all__',    # EXAMPLE = 'COUNTRY_CODE_1, COUNTRY_CODE_2' 
        'BLACK_LIST': '__none__',   # EXAMPLE = '__all__' OR 'COUNTRY_CODE_3, COUNTRY_CODE_4'
    },
}
 ```

### Migrate

```
python manage.py migrate
```

### SMS

#### Support

1. [SNS AWS](https://aws.amazon.com/sns/)
1. [Twilio](https://www.twilio.com/sms)

#### How to use it?

Base on sample config, two sms send from `twilio` with `TWILIO_EE_SENDER` number and one of them from `AWS-SNS` and region is `eu-west-1`.
 
```python
from azmessaging import default_settings as settings
from azmessaging.models import SMSNotificationType
identifier = 'what ever you want'
message = 'Your code is: 1222'
sms_type = SMSNotificationType.TRANSACTIONAL
klass = settings.READER.klass('sms', identifier)
sms = klass(identifier=identifier, message=message, sms_type=sms_type)
sms.set_receivers(['+16503331111', '+37211123450', '+37211123451'])
sms.notify()
```

### Telegram


#### How to use it?
 
```python
from azmessaging import default_settings as settings
identifier = 'what ever you want'
message = 'Your code is: 1222'
klass = settings.READER.klass('telegram', identifier)
telegram = klass(identifier=identifier, message=message)
telegram.set_receivers(['user_a', 'user_b', ])
telegram.notify()
```

# TODO

- [ ] Documentation

- [x] Support multiple provider 

- [X] SMS Support

- [X] SMS Support SNS AWS

- [X] SMS Support Twilio

- [X] SMS Routing Base on country/continents

- [x] SMS Support every provider you want.

- [X] SMS Batch 

- [ ] Push notification

- [ ] Console

- [ ] Websocket

- [X] Telegram

## Develop

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.


