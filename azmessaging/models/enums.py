from azmessaging import default_settings as settings

class SMSNotificationType(settings.TEXT_CHOICES):
    PROMOTIONAL = 'PROMOTIONAL'
    TRANSACTIONAL = 'TRANSACTIONAL'
