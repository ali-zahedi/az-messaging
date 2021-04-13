<!--![GitHub All Releases](https://img.shields.io/github/downloads/ali-zahedi/az-iranian-bank-gateways/total)-->
<!--![GitHub issues](https://img.shields.io/github/issues/ali-zahedi/az-iranian-bank-gateways)-->
![GitHub](https://img.shields.io/github/license/ali-zahedi/az-messaging)
![GitHub](https://img.shields.io/pypi/pyversions/az-messaging.svg?maxAge=2592000)
![GitHub](https://img.shields.io/pypi/v/az-messaging.svg?maxAge=2592000)
# AZ Messaging config

[[_TOC_]]


``pip install az-messaging``


### settings.py

 
 ``` python
INSTALLED_APPS = [
    # ....
    'azmessaging',
    # ...
]

AZ_MESSAGING = {
    'CLASS': {
        'SMS': 'azmessaging.channels.SMSNotificationChannel',
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
                        'countries': 'DE',
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
        ]
    },
}
 ```

### Migrate

```
python manage.py migrate
```


# TODO

- [ ] Documentation

- [ ] Support multiple provider 

- [X] SMS Support

- [X] SMS Support SNS AWS

- [X] SMS Support Twilio

- [X] SMS Base on country

- [X] SMS Batch 

- [ ] Push notification

- [ ] Console

- [ ] Websocket

- [ ] Telegram bot

## Develop

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.


