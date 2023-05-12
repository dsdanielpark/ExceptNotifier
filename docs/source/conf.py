# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# This will include the necessary source files folders in the PATH to be able to generate the documentation from.
# devdir=r'C:\Users\parkm\Desktop\git\ExceptionNotifier'
# try:
#     if os.environ['DEVDIR']:
#         devdir = os.environ['DEVDIR']
# except KeyError:
#     print('Unable to obtain $DEVDIR from the environment.')
#     pass

sys.path.insert(0, os.path.abspath("../.."))
# sys.path.insert(0, os.path.abspath('../ExceptNotifier/__init__.py'))
sys.setrecursionlimit(1500)


# Ensure that the __init__ method gets documented.
def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    return skip


# -- Project information -----------------------------------------------------

project = "ExceptNotifier"
copyright = "2023, MinWoo Park"
author = "MinWoo Park"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "**tests**", "**spi**"]

# The full version, including alpha/beta/rc tags
release = "0.2.11"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.todo", "sphinx.ext.autosummary"]


# import mock

# MOCK_MODULES = ['sphinx-rtd-theme', 'repoze.sphinx.autointerface', 'sphinxcontrib-autoprogram', 'Sphinx', 'dbus-python', 'docutils', 'ExceptNotifier']
# for mod_name in MOCK_MODULES:
#     sys.modules[mod_name] = mock.Mock()

autosummary_generate = True  # Turn on sphinx.ext.autosummary

# ,'sphinx.ext.napoleon'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
todo_include_todos = True
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# sys.path.insert(0, os.path.abspath(r'C:\Users\parkm\Desktop\git\ExceptionNotifier\ExceptNotifier'))


# # RTD option args
# html_theme_options = {
#     # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#     # 'analytics_anonymize_ip': False,
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     'style_nav_header_background': 'white',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': False,
#     'titles_only': True
# }


# # When need app setup
# class GithubURLDomain(Domain):
#     """
#     Resolve .py links to their respective Github URL
#     """

#     name = "githuburl"
#     ROOT = "https://github.com/UKPLab/sentence-transformers/tree/master"

#     def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
#         if (target.endswith('.py') or target.endswith('.ipynb')) and not target.startswith('http'):
#             from_folder = os.path.dirname(fromdocname)
#             contnode["refuri"] = "/".join([self.ROOT, from_folder, target])
#             return [("githuburl:any", contnode)]
#         return []


# def setup(app):
#     app.add_domain(GithubURLDomain)
#     app.add_config_value('recommonmark_config', {
#             #'url_resolver': lambda url: github_doc_root + url,
#             'auto_toc_tree_section': 'Contents',
#             }, True)
#     app.add_transform(AutoStructify)
