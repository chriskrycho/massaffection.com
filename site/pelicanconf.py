#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Krycho'
SITENAME = 'Mass Affection'
SITE_DESCRIPTION = 'A husband and wife play-through of the Mass Effect games. Laughter, romance, and hijinks ensue. Biweekly episodes discussing plot, character, gameplay—the whole gamut!'
SITEURL = ''

CDN_DOMAIN = 'cdn.massaffection.com'
CDN_URL = 'http://' + CDN_DOMAIN
CDN_TLS_URL = 'https://massaffection-cdn.objects-us-west-1.dream.io'

LOGO_URL = CDN_URL + '/cover.jpg'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_LANG = 'en'

THEME = '../ma_theme'

THEME_STATIC_DIR = ''

# No categories or tags
DIRECT_TEMPLATES = ['index', 'categories']
PAGINATED_DIRECT_TEMPLATES = ['index', 'categories']

SLUGIFY_SOURCE = 'basename'

ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
ARTICLE_URL = '{category}/{slug}/'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Disable unused pages
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

DEFAULT_CATEGORY = 'News'


# All feeds for this particular site are disabled; I generate the feeds via
# [Feeder] -- at least until such a time I create a podcast plugin for Pelican.
# (Frankly, that might be never.)
#
# [Feeder]: http://reinventedsoftware.com/feeder/
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 12  # roughly 3 months. Ish.

STATIC_PATHS = ['extra/CNAME',
                'extra/favicon.ico',
                'extra/.nojekyll',
                'extra/feed.xml',
                ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/feed.xml': {'path': 'feed.xml'},
                       'extra/.nojekyll': {'path': '.nojekyll'},
                       }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.meta': {},
    },
}