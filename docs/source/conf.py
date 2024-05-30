import os
import sys
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Web3 Transfer Agent Depository'
copyright = '2024, BlockTrans Syndicate'
author = 'Block Transfer'

# Release and version
release = '0.1'
version = '0.1.0'

# Extensions
extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
]

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Source suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Templates path
templates_path = ['_templates']

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_depth': 4,
    'style_nav_header_background': '#AC51FF',
    'head_font_family': 'Montserrat, sans-serif',
    'link': '#AC51FF',
    'link_hover': '#682D8B',
}
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'

# EPUB output options
epub_show_urls = 'footnote'

# Master document
master_doc = 'index'

# Custom setup function
def setup(app):
    app.add_transform(AutoStructify)
    # If you need custom CSS, uncomment and modify the lines below
    # app.add_css_file('custom.css')
    # html_context = {
    #     'css_files': [
    #         'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap',
    #     ],
    # }
