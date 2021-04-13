import importlib

import pytz


def import_class(path):
    package, attr = path.rsplit('.', 1)
    klass = getattr(importlib.import_module(package), attr)
    return klass


def get_continent(country_code):
    continent = pytz.country_timezones[country_code][0].split('/')[0]
    return continent
