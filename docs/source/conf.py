# -- Project information

project = 'TAD3'
copyright = '2024'
author = 'BlockTrans Syndicate'

release = '0.1'
version = '0.1.0'

extensions = [
    'recommonmark',
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

html_static_path = ['_static']
html_favicon = '_static/favicon.ico'

# CSS not working RN
# def setup(app):
#     app.add_css_file('custom.css')
#
# html_context = {
#     'css_files': [
#         'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap',
#     ],
# }
