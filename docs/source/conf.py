# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Curso de Arduino'
copyright = '2023, Felipe Cavalcante'
author = 'Felipe Cavalcante'

release = '0.1'
version = '0.1.0'

# -- General configuration
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo', 
	'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

todo_include_todos = True
todo_link_only = True

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'classic'
#html_theme = 'nature'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_search_language = 'pt'
language = 'pt_BR'

html_show_copyright = False

autosummary_generate = True


html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
