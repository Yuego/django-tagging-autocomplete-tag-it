#coding: utf-8
from __future__ import unicode_literals, absolute_import

__all__ = []

from django.db.models import FieldDoesNotExist
from tagging.models import Tag

try:
    tagging_has_namespace = True
    Tag._meta.get_field_by_name('namespace')
except FieldDoesNotExist:
    tagging_has_namespace = False
