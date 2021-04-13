class AZMessagingException(Exception):
    """AZ Messaging exception"""

class AZSettingDoesNotExist(AZMessagingException):
    """The requested setting does not exist"""
