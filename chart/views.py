from django.shortcuts import render

import parser.model
from models import Region, Country

REGION_KEY = u"Регион"
COUNTRY_KEY = u"Страна"
VALUE_KEY = u"Значение"


def update_db(filepath):
    data, structure = parser.model.Parser.get_from_file(filepath)
    generate_db_content(data)


def generate_db_content(data):
    """
    :param data:[{Регион:.., Страна:.., Значение:..}...]
    :return:
    """
    map(add_info, data)


def add_info(info):
    region_name = info[REGION_KEY]
    region = add_region(region_name)
    add_country(region, info)


def add_region(region_name):
    if not Region.objects.filter(name=region_name):
        region = Region(name=region_name)
        region.save()
    else:
        region = Region.objects.get(name=region_name)
    return region


def add_country(region, info):
    country_name = info[COUNTRY_KEY]
    value = info[VALUE_KEY]
    if not Country.objects.filter(name=country_name):
        Country(region=region, name=country_name, value=value)