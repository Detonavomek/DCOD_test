from django.conf.urls import patterns, include, url
from django.contrib import admin

from chart import views

urlpatterns = patterns('',
    url(r'(?P<region_name>[\w -]+)$', views.show_region, name='region'),
    url(r'^$', views.show_region, name='region'),
    url(r'^admin/', include(admin.site.urls)),
)
