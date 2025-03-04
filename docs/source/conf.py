# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mnflow'
copyright = '2024, Aryan Mehboudi'
author = 'Aryan Mehboudi'
release = '0.0.1.2'

# import sys
# import os
# sys.path.append(os.path.abspath('..'))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'myst_nb',
    # 'nbsphinx',
    # 'myst-parser',
]

#
templates_path = ['_templates']
exclude_patterns = ['demo/**/*',]

# https://myst-nb.readthedocs.io/en/latest/authoring/basics.html#authoring-intro
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.ipynb': 'myst-nb',
#     '.myst': 'myst-nb',
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# ------------------------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoclass
#
# autoclass_content
# This value selects what content will be inserted into the main body of an autoclass directive.
# ------------------------------------------------------------------------------------------
autoclass_content='both' #Both the class’ and the __init__ method’s docstring are concatenated and inserted.

# -- Options for autodoc ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

# Automatically extract typehints when specified and place them in
# descriptions of the relevant function/method.
#autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "mixed"

# Enable numref
numfig = True


#--- LaTeX preamble
# https://stackoverflow.com/questions/28454217/how-to-avoid-the-too-deeply-nested-error-when-creating-pdfs-with-sphinx
# https://github.com/sphinx-doc/sphinx/issues/2304
latex_elements = {
# Additional stuff for the LaTeX preamble.
'preamble': r'\usepackage{enumitem}\setlistdepth{99}'  #+\
    #'\\usepackage[draft]{minted}\\fvset{breaklines=true}',
# https://stackoverflow.com/questions/43153472/how-do-i-fix-the-margins-on-pdfs-created-by-sphinx-easily
# 'printindex': '\\footnotesize\\raggedright\\printindex',
}