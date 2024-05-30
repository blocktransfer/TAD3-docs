import os
import sys
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('.'))

project = 'Web3 Transfer Agent Depository'
copyright = '2024, BlockTrans Syndicate'
author = 'BlockTrans Syndicate'

release = '0.1'
version = '0.1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
master_doc = 'index'
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'
exclude_patterns = ['index.md']
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

def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
    
# CSS not working RN
# def setup(app):
#     app.add_css_file('custom.css')
#
# html_context = {
#     'css_files': [
#         'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap',
#     ],
# }
