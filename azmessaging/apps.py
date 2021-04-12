# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AZMessagingConfig(AppConfig):
    name = 'azmessaging'
    verbose_name = _('AZ Messaging')
    verbose_name_plural = _('AZ Messaging')
