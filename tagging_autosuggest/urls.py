#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import *

urlpatterns = patterns('tagging_autosuggest.views',
    url(r'^suggest$', 'suggest', name='tagging_autosuggest-suggest'),
)
