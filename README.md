# django-tagging-autocomplete-tag-it

Fork of *[django-tagging-autocomplete](http://code.google.com/p/django-tagging-autocomplete/)* that works with a modified version (another fork) jQuery UI Tag-it.

**This is not stable**. If you would like to use this widget please share your ideas (and code) on how to improve it.

## Demo:

To see the jQuery UI widget in action its demos: [http://aehlke.github.com/tag-it/](http://aehlke.github.com/tag-it/)
The forked repository for the javascript is: [https://github.com/nemesisdesign/tag-it](https://github.com/nemesisdesign/tag-it)

## Features:
* Tag editing
* Autocompletition
* Customizable minimum amount of letters before the autocompletition starts
* Customizable maximum tags number
* Costomizable max length of each tag
* Aims to be flexible

## Available settings:

    TAGGING_AUTOCOMPLETE_MIN_LENGTH defaults to 1
    TAGGING_AUTOCOMPLETE_REMOVE_CONFIRMATION defaults to True
    TAGGING_AUTOCOMPLETE_ANIMATE defaults to True
    TAGGING_AUTOCOMPLETE_MAX_TAGS defaults to 20 - this general setting can be overriden in each field if needed
    TAGGING_AUTOCOMPLETE_JS_BASE_URL defaults to 'STATIC_URL/js/jquery-tag-it/'
    TAGGING_AUTOCOMPLETE_JQUERY_UI_FILE defaults to 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
    TAGGING_AUTOCOMPLETE_CSS is a list of CSS files and defaults to ['TAGGING_AUTOCOMPLETE_JS_BASE_URL/css/ui-autocomplete-tag-it.css']

## Usage

I wrote these instructions quickly, don't trust this completely.

###Usage in models:

    # models.py
    from django.db import models
    from tagging_autocomplete_tagit.models import TagAutocompleteTagItField

    class SomeModel(models.Model):
            # max_tags defaults to TAGGING_AUTOCOMPLETE_MAX_TAGS
            # If max_tags is specified it will override the value specified in TAGGING_AUTOCOMPLETE_MAX_TAGS
            tags = TagAutocompleteTagItField(max_tags=False)

###Using the form widget:

Alternatively you can use the TagAutocomplete form widget while creating your form. For example:

    # forms.py
    from django import forms
    from tagging.forms import TagField
    from tagging_autocomplete_tagit.widgets import TagAutocompleteTagIt

    class SomeForm(forms.Form):
        # max_tags defaults to TAGGING_AUTOCOMPLETE_MAX_TAGS
        # If max_tags is specified it will override the value specified in TAGGING_AUTOCOMPLETE_MAX_TAGS
        tags = TagField(widget=TagAutocompleteTagIt(max_tags=5))

##Instalation

   1. You need to have django-tagging already installed
   2. Download django-tagging-autocomplete-tag-it and use setup.py to install it on your system:
		python setup.py install
        (NOT SURE THIS WORKS NOW)
   4. Copy "jquery-tag-it" folder of this repository to the 'js' folder specified in your project's STATIC_URL setting. If you want to put it somewhere else add TAGGING_AUTOCOMPLETE_JS_BASE_URL to your project settings.
   5. Add "tagging_autocomplete_tagit" to installed apps in your project's settings.
   6. Add the following line to your project's urls.py file:

      (r'^tagging_autocomplete_tagit/', include('tagging_autocomplete_tagit.urls')),
