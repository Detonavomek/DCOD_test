from django.conf.urls import patterns, include, url
from django.contrib import admin

from chart import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dcod_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.base, name='home'),
    url(r'region/(?P<region>[\w -]+)$', views.show_region, name='region'),
    url(r'^admin/', include(admin.site.urls)),
)
