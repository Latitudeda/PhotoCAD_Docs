# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PhotoCAD'
copyright = '2022, Latitudeda.com'
author = 'latitudeda.com'

release = '1.6'
version = '1.6.0'


# -- General configuration

extensions = [
    'multiproject',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

multiproject_projects = {
    "en": {
        "use_config_file": False,
    },
    "zh": {
        "use_config_file": False,
    },
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_js_files = [
    'https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.6.2.min.js',
]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
}

# current_project = get_project(multiproject_projects)

# if current_project == "en":
#     language = "en"
# elif current_project == "dev":
#     language = "es"
