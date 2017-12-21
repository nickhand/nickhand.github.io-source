#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Hand'
SITEURL = ''
SITENAME = "Offhand Remarks"
SITETITLE = AUTHOR
SITESUBTITLE = 'Astrophysics PhD, Aspiring Data Scientist'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
# SITELOGO = '/blog/images/profile.jpg'
BROWSER_COLOR = '#333333'


AUTHOR = 'Nick Hand'
SITENAME = 'Offhand Remarks'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
DISPLAY_HOME_ON_MENU = False
HOME_HIDE_TAGS = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (('Home', '/index.html#page-welcome'),
             ('Archives', '/blog/archives.html'),
             ('Categories', '/blog/categories.html'),
             ('Tags', '/blog/tags.html'),)

LINKS = (('About me', '/index.html#page-welcome'),
)


COPYRIGHT_YEAR = 2017
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PLUGIN_PATHS = ['./blog/plugins/pelican-plugins', './blog/plugins/']
PLUGINS = [
    'summary',
    'i18n_subsites',
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]

IGNORE_FILES = ['.ipynb_checkpoints']

THEME = './blog/theme'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

ROOT = "/blog/"
SHOW_ARCHIVES = True
CONTACT_PAGE = "/index.html#page-contact"
ABOUT_PAGE = "/index.html#page-profile"


# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

DEFAULT_PAGINATION = 10

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

RELATIVE_URLS = True
