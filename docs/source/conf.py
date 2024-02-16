# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Comparative Mythology'
copyright = '2024, Anindita Basu'
author = 'Anindita Basu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_favicon'
]

myst_enable_extensions = ['colon_fence']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# See https://sphinx-book-theme.readthedocs.io/en/stable/tutorials/get-started.html
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/AninditaBasu/comparative-mythology",
    "use_repository_button": False,
    "use_download_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "repository_branch": "main",
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    #"extra_navbar": "<a href='about.html'>About me</a>",
    "toc_title": "On this page",
    "show_toc_level": 2,
}
html_sidebars = {
    "**": ["navbar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]
}

myst_html_meta = {
    "description lang=en": "A linguistic, psychological, structural, phylogenetical, naturalistic, and historical and comparative analysis of the mythology of the world",
    "keywords": "mythology, comparative mythology",
    "property=og:locale":  "en_US",
    "image": "_static/logo.jpg"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_title = 'Home'
html_logo = '_static/logo.jpg'

favicons = [
    {
        "rel": "icon",
        "static-file": "favicon.ico",
        "type": "image/png",
    },
]