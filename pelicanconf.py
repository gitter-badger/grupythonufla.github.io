#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

AUTHOR = u'Grupython UFLA'
SITENAME = u'Grupython UFLA'
SITEURL = ''

META_DESCRIPTION = '''O Grupython UFLA é uma comunidade de usuários (profissionais e
                      amadores) da linguagem Python, onde prezamos pela troca de
                      conhecimento, respeito mútuo e diversidade (tanto de opinião
                      quanto de tecnologias).'''

META_KEYWORDS = ['grupython', 'python', 'ufla', 'desenvolvimento']

TIMEZONE = 'America/Sao_Paulo'
THEME = 'themes/malt'
MALT_BASE_COLOR = 'grey'

SITE_LOGO = 'images/logo/logo.png'
SITE_LOGO_MOBILE = 'images/logo/logo-inv.png'

STATIC_PATHS = ['images']

WELCOME_TITLE = 'Seja bem vindo ao {}!'.format(SITENAME)
WELCOME_TEXT = 'Grupo de usuários da linguagem Python da Universidade Federal de Lavras.'
SITE_BACKGROUND_IMAGE = 'images/banners/background.png'
FOOTER_ABOUT = '''O Grupython UFLA é uma comunidade de usuários (profissionais e
                  amadores) da linguagem Python, onde prezamos pela troca de
                  conhecimento, respeito mútuo e diversidade (tanto de opinião
                  quanto de tecnologias).'''

DEFAULT_LANG = u'pt'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
    'better_figures_and_images',
    'sitemap',
]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

GITHUB_REPO = "http://github.com/grupythonufla/grupythonufla.github.io"
GITHUB_BRANCH = "pelican"
OPEN_GRAPH_IMAGE = "/images/logo/logo-inv.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title": "Comunidade",
        "href": "comunidade",
    },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://www.facebook.com/grupythonufla",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://github.com/grupythonufla",
        "icon": "fa-github",
        "text": "GitHub",
    },
    # {
    #     "href": "http://grupydf.slack.com",
    #     "icon": "fa-slack",
    #     "text": "Slack",
    # },
)

MEMBROS = OrderedDict((
    ("Cássio Botaro", {
        "email": "cassiobotaro@gmail.com",
        "twitter": "@cassiobotaro",
        "github": "cassiobotaro",
        "site": {
            "nome": "Import None",
            "href": "http://cassiobotaro.github.io",
            }
        }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade do GrupyDF se comunica através de mailing " +\
                    "lists, grupo no telegram e no slack, mas frequentemente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade do GrupyDF, apesar de extensa possui alguns " +\
                        "colaboradores principais, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": " Atualmente o GrupyDF possui poucos projetos em andamento:" +\
                        "Traduções do Django-docs e Python on Campus.",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
]

from themes.malt.functions import *
