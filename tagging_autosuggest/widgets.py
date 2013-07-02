#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.forms.widgets import TextInput
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe

from .models import tagging_has_namespace


class TagAutosuggestTagIt(TextInput):
    
    def __init__(self, max_tags, *args, **kwargs):
        self.max_tags = max_tags if max_tags else getattr(settings, 'TAGGING_AUTOSUGGEST_MAX_TAGS', 20)
        self.namespace = kwargs.pop('namespace', None)
        super(TagAutosuggestTagIt, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        """ Render HTML code """
        # django-tagging
        case_sensitive = 'true' if not getattr(settings, 'FORCE_LOWERCASE_TAGS', False) else 'false'
        max_tag_lentgh = getattr(settings, 'MAX_TAG_LENGTH', 50)
        # django-tagging-autocomplete-tagit
        autocomplete_min_length = getattr(settings, 'TAGGING_AUTOSUGGEST_MIN_LENGTH', 1)
        remove_confirmation = 'true' if getattr(settings, 'TAGGING_AUTOSUGGEST_REMOVE_CONFIRMATION', True) else 'false'
        animate = 'true' if getattr(settings, 'TAGGING_AUTOSUGGEST_ANIMATE', True) else 'false'
        allow_spaces = 'true' if getattr(settings, 'TAGGING_AUTOSUGGEST_ALLOW_SPACES', True) else 'false'

        list_view = reverse('tagging_autosuggest-suggest')

        if tagging_has_namespace and self.namespace is not None:
            list_view = '{0}?ns={1}'.format(list_view, self.namespace)

        html = super(TagAutosuggestTagIt, self).render(name, value, attrs)
        # Subclass this field in case you need to add some custom behaviour like custom callbacks
        js = u"""<script type="text/javascript">init_jQueryTagit({
                allowSpaces: %s,
                objectId: '%s',
                sourceUrl: '%s',
                fieldName: '%s',
                minLength: %s,
                removeConfirmation: %s,
                caseSensitive: %s,
                animate: %s,
                maxLength: %s,
                maxTags: %s,
                onTagAdded  : null,
                onTagRemoved: null,
                onTagClicked: null,
                onMaxTagsExceeded: null,
            })
            </script>""" % (allow_spaces, attrs['id'], list_view, name, autocomplete_min_length, remove_confirmation, case_sensitive,
                            animate, max_tag_lentgh, self.max_tags)
        return mark_safe("\n".join([html, js]))
    
    class Media:
        # JS Base url defaults to STATIC_URL/jquery-autocomplete/
        js_base_url = getattr(settings, 'TAGGING_AUTOSUGGEST_JS_BASE_URL', '{0}tagging_autosuggest/js/'.format(settings.STATIC_URL))
        # jQuery ui is loaded from google's CDN by default
        jqueryui_default = '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js'
        jqueryui_file = getattr(settings, 'TAGGING_AUTOSUGGEST_JQUERY_UI_FILE', jqueryui_default)
        # if a custom jquery ui file has been specified
        if jqueryui_file != jqueryui_default:
            # determine path
            jqueryui_file = '%s%s' % (js_base_url, jqueryui_file)
        
        # load js
        js = (
            '%stagging_autosuggest.js' % js_base_url,
            jqueryui_file,
            '%sjquery.tag-it.min.js' % js_base_url,            
        )
        
        # custom css can also be overriden in settings
        css_list = getattr(settings, 'TAGGING_AUTOSUGGEST_CSS', ['{0}tagging_autosuggest/css/ui-autocomplete-tag-it.css'.format(settings.STATIC_URL)])
        # check is a list, if is a string convert it to a list
        if type(css_list) != list and type(css_list) == str:
            css_list = [css_list]
        css = {
            'screen': css_list
        }