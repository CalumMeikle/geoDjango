# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Shop


latitude = 53.37828541667638
longitude = -1.4629411697387695

user_location = Point(longitude, latitude, srid=4326)
#https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API for geolocatin api, you'd need a GDPR thing for this

class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
    template_name = 'shops/index.html'
