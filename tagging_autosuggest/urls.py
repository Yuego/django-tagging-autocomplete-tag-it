from django.conf.urls.defaults import *

urlpatterns = patterns('tagging_autosuggest.views',
    url(r'^suggest$', 'suggest', name='tagging_autosuggest-suggest'),
)
