project = "Web3 Transfer Agent Depository"
author = "BlockTransfer"
copyright = "2024, BlockTrans Syndicate"

version = "0.1.0"
release = version

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]

myst_enable_extensions = [
    "colon_fence",
]

source_suffix = {
    ".md": "markdown",
}
master_doc = "index"
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "navigation_depth": 4,
    "style_nav_header_background": "#AC51FF",
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.ico"

epub_show_urls = "footnote"
