# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thermodynamics: theoretical pills'
copyright = '2025, TEFLU'
author = 'TEFLU'

# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgconverter',
    'hoverxref.extension'
]

# Make formal refs hoverable without changing markup.
hoverxref_auto_ref = True
hoverxref_roles = ["eq"]                # add others like "numref" if you want
hoverxref_role_types = {"eq": "tooltip"}
hoverxref_mathjax = True                # re-render MathJax inside the tooltip

# Configure MathJax for equation numbering and cross-references
# mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML'
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# MyST Configuration
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
]