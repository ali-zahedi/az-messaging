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
    
}
 ```

### Migrate

```
python manage.py migrate
```


# TODO

- [ ] Documentation

- [ ] Support multiple provider 

- [ ] SMS Support

- [ ] SMS Support SNS AWS

- [ ] SMS Support Twilio

- [ ] SMS Base on country

- [ ] SMS Batch 

- [ ] Push notification

- [ ] Console

- [ ] Websocket

- [ ] Telegram bot

## Develop

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.


