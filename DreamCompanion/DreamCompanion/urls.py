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
# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
]