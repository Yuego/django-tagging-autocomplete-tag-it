#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.admin.widgets import AdminTextInputWidget

from tagging.fields import TagField
from tagging_autosuggest.widgets import TagAutosuggestTagIt

from .models import tagging_has_namespace

# The following code is based on models.py file from django-tinymce by Joost Cassee


class TagAutosuggestField(TagField):
    """
    TagField with jQuery UI Tag-it widget
    """
    
    def __init__(self, max_tags=False, *args, **kwargs):
        self.max_tags = max_tags
        super(TagAutosuggestField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        widget_kwargs = {
            'max_tags': self.max_tags,
        }
        if hasattr(self, 'namespace'):
            widget_kwargs.update({
                'namespace': self.namespace
            })
        defaults = {'widget': TagAutosuggestTagIt(**widget_kwargs)}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagAutosuggestTagIt(**widget_kwargs)

        return super(TagAutosuggestField, self).formfield(**defaults)