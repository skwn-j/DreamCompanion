"""
Definition of urls for DreamCompanion.
"""

from datetime import datetime
from django.conf.urls import include, url
import django.contrib.auth.views
import HelloDjangoApp.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name = 'index'),
    url(r'^home$', HelloDjangoApp.views.index, name = 'home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
