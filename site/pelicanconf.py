#!/usr/bin/env python

from copy import copy
from pathlib import Path
import re
import sys

# Setup path to enable local helpers.
sys.path.append(str(Path(__file__).parent))

import helpers


AUTHOR = 'Chris Krycho'
SITENAME = 'Mass Affection'
SITE_DESCRIPTION = '''
A husband and wife play-through of the Mass Effect games. Laughter, romance, \
and hijinks ensue. Biweekly episodes discussing plot, character, gameplay—the \
whole gamut!'''
SITEURL = ''

CDN_DOMAIN = 'massaffection-cdn.objects-us-west-1.dream.io'
CDN_URL = 'https://' + CDN_DOMAIN

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

EMBED_DIR_NAME = 'embed'
STATIC_PATHS = ['extra/CNAME',
                'extra/favicon.png',
                'extra/.nojekyll',
                'extra/feed.xml',
                'extra/challenge',
                'extra/challenge-www',
                EMBED_DIR_NAME,
                ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/feed.xml': {'path': 'feed.xml'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/challenge': {
        'path': '.well-known/acme-challenge/OyLLMakXI6WnReHGiLYqy5GwhsaS2ot_gbLNBnJpDF0.html',
        'path': '.well-known/acme-challenge/AesnLB6GRuIwCjQzpRycjkrDXhJxvUlJtMS56yT-KHI.html'
    },
}

ARTICLE_EXCLUDES = [EMBED_DIR_NAME]
PAGE_EXCLUDES = [EMBED_DIR_NAME]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.meta': {},
    },
}


# Generate embed items for every episode.
site_dir = Path(__file__).parent
content_dir = site_dir / 'content'
all_content_paths = list(content_dir.glob('*.md'))
podcast_paths = [p for p in all_content_paths if helpers.is_podcast(p)]
embeds = {
    p.name: helpers.embed(
        p.with_suffix('.mp3').name, 
        LOGO_URL,
        CDN_URL) for p in podcast_paths
}
embed_dir = content_dir / EMBED_DIR_NAME

helpers.check_embed_dir(embed_dir)
print('\ngenerating embed files at {}:\n'.format(str(embed_dir)))
for name, embed in embeds.items():
    fpath = (embed_dir / name).with_suffix('.html')
    print('  - {}'.format(name))
    with fpath.open('w') as fd:
        fd.write(embed)
print()