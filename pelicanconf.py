#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'John ZuHone'
SITENAME = u'John A. ZuHone'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/astrojaz'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#THEME = "/Users/jzuhone/Source/pelican-themes/pelican-bootstrap3"
THEME = "gum"

PLUGIN_PATH = "/Users/jzuhone/Source/pelican-plugins"
PLUGINS = ["latex","pelican_vimeo"]

RESPONSIVE_IMAGES=True

STATIC_PATHS = ["images","files"]

TWITTER_URL = 'http://twitter.com/astrojaz'
