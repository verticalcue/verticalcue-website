#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = u'VerticalCue Design'
SITENAME = u'VerticalCue Design'
SITEURL = 'http://www.verticalcue.com'
COPYRIGHT = '&copy; 2009-{0} VerticalCue Design LLC'.format(
    time.strftime('%Y'))

PATH = 'content'
THEME = 'themes/verticalcue-2013'

TIMEZONE = 'America/Chicaco'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
