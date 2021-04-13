# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AZMessagingConfig(AppConfig):
    name = 'azmessaging'
    verbose_name = _('AZ Messaging')
    verbose_name_plural = _('AZ Messaging')

    def ready(self):
        from azmessaging import default_settings as settings
        from azmessaging.utils import import_class
        settings.READER = import_class(settings.SETTING_VALUE_READER_CLASS)()
