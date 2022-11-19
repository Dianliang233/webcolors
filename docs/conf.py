import sys

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "sphinx.ext.viewcode"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "webcolors"
copyright = "2008-2022, James Bennett"
version = "1.13"
release = "1.13a1"
exclude_trees = ["_build"]
pygments_style = "sphinx"
htmlhelp_basename = "webcolorsdoc"
latex_documents = [
    ("index", "webcolors.tex", "webcolors Documentation", "James Bennett", "manual"),
]
html_theme = "furo"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist.txt"
