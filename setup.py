# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from tagging_autosuggest.version import __version__
 
setup(
    name='django-autosuggest',
    version=__version__,
    description='Autocompletion for django-tagging',
    long_description=open('README.rst').read(),
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='http://code.google.com/p/django-tagging-autocomplete/',
    packages=find_packages(),
    include_package_data=True,
    requires=[
        'django (>=1.4)',
        'tagging (>=0.5.0)',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
) 
