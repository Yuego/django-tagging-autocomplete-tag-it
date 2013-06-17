#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.admin.widgets import AdminTextInputWidget

from tagging.fields import TagField
from tagging_autosuggest.widgets import TagAutosuggestTagIt

# The following code is based on models.py file from django-tinymce by Joost Cassee


class TagAutosuggestField(TagField):
    """
    TagField with jQuery UI Tag-it widget
    """
    
    def __init__(self, max_tags=False, *args, **kwargs):
        self.max_tags = max_tags
        super(TagAutosuggestField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {'widget': TagAutosuggestTagIt(max_tags=self.max_tags)}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagAutosuggestTagIt(max_tags=self.max_tags)

        return super(TagAutosuggestField, self).formfield(**defaults)