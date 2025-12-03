# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thermal and Fluids Engineering: Theoretical Pills'
copyright = '2025, Mondragon Goi Eskola Politeknikoa (MGEP), TEFLU'
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
    'sphinx_togglebutton',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.bibtex',
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    # 'sphinx.ext.imgconverter',
    "sphinxcontrib.cairosvgconverter",
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

# Sphinx + MathJax v3: auto-number AMS equations and use labels as IDs
mathjax3_config = {
    "tex": {
        "tags": "ams",         # "none", "ams", or "all"
        "useLabelIds": True,   # use \label or directive labels as anchor IDs
        "packages": {"[+]": ["cancel"]},   # <-- enable \cancel
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],  # allow $...$ too
    }
}

# Optional: number all displayed math regardless of \begin{equation}
math_number_all = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
    'titles_only': False,
}

# MyST Configuration
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
    "deflist",
    "tasklist",
    "substitution",
    "html_admonition",
    "html_image",
]

# Tell togglebutton which elements should collapse
togglebutton_selector = (
    ".admonition.dropdown, "        # MyST admonitions with :class: dropdown
    "details.dropdown"              # (if you also use <details> via MyST)
)

# Optional: start them open/closed, show an icon, etc.
togglebutton_hint = ""
togglebutton_hint_none = True

# Point to your .bib file(s)
bibtex_bibfiles = ["references.bib"]

# Formatting settings
bibtex_default_style = "unsrt"
bibtex_reference_style = "label"

latex_engine = "xelatex"

# LaTeX settings.
latex_elements = {
    
    "preamble": r"""
        \usepackage{graphicx}
        
        % Save original macro
        \let\origSphinxSection\sphinxsection

        % Redefine it with custom spacing
        \renewcommand{\sphinxsection}[2]{
          \vspace*{1.2em}       % space BEFORE the section title
          \origSphinxSection{#1}{#2}
          \vspace{0.2em}        % space AFTER the section title
        } 
        """,
    
    "tableofcontents": r"""
        \begingroup
          \setcounter{tocdepth}{1} % 0=chapter, 1=section, 2=subsection, ...
          \sphinxtableofcontents
        \endgroup
        """,    
    
    "sphinxsetup": r"""
        noteBgColor={RGB}{230,240,255},
        noteBorderColor={RGB}{60,110,200},
        noteborder=0.8pt,
        importantBgColor={RGB}{253,246,200},
        importantBorderColor={RGB}{204,153,0},
        importantborder=0.8pt,
        tipBgColor={RGB}{226,244,226},
        tipBorderColor={RGB}{70,140,70},
        tipborder=0.8pt,
        warningBgColor={RGB}{253,246,200},
        warningBorderColor={RGB}{204,153,0},
        warningborder=1pt,  
        """,
    
    "fontpkg": r"""
        \setmainfont{TeX Gyre Pagella}
        \setsansfont{TeX Gyre Heros}
        \setmonofont{Fira Code}
    """,
    
    # Optional: paper size, base font size
    "papersize": "a4paper",
    "pointsize": "11pt",    
}

latex_documents = [
    ("index",
     "teflu.tex",
     "Thermal and Fluids Engineering: Theoretical Pills",
     "Mondragon Goi Eskola Politeknikoa, TEFLU",
     "manual",
     False),
]