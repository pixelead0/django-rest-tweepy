"""
  settings URL Configuration
  Author  :   Adan GQ <adangq@gmail.com>
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

urlpatterns = ([
     url(r'^admin/', admin.site.urls)
])
