# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from tagging_autosuggest.version import __version__

long_description = open('README.txt').read()
 
setup(
    name='django-tagging-autocomplete',
    version=__version__,
    description='Autocompletion for django-tagging',
    long_description=long_description,
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='http://code.google.com/p/django-tagging-autocomplete/',
    packages=find_packages(),
    include_package_data=True,
    requires=[
        'django (>=1.4)',
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
    zip_safe=False,
) 
