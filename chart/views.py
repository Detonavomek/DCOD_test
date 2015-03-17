# -*- coding:utf-8 -*-
import json

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse

import parser.model
from models import Region, Country
from . import DATA_FILE

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
    value = float(info[VALUE_KEY])
    if not Country.objects.filter(name=country_name):
        country = Country(region=region, name=country_name, value=value)
        country.save()


def base(request):
    regions = [region.name for region in Region.objects.all()]
    return render_to_response("base.html", locals())


def show_region(request, region):
    regions = [region.name for region in Region.objects.all()]
    data = dict()
    try:
        region_db = Region.objects.get(name=region)
        countries = {country.name: country.value
                     for country in region_db.country_set.all()}
        data[region] = countries
    except Region.DoesNotExist, error:
        return render_to_response(request, locals())
    finally:
        data = json.dumps(data)
        # regions = [region.name for region in Region.objects.all()]
        return render_to_response("regions.html", locals())

# def show_regions(request, region_name):
#     region = Region.objects.get(name=region_name)
#     countries = region.country_set.all()
#     data = {region.name:
#                 {country.name: country.value for country in countries}}
#     data = json.dumps(data)
#     # return HttpResponse(data, content_type='application/json')
#     # return HttpResponse(data, mimetype='application/json')
#     return JsonResponse(data)
#     # return render_to_response("base.html", data, content_type='application/json')