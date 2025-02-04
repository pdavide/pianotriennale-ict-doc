# Add this line at the top of the file within the "import" section
import docs_italia_theme

# Add the Sphinx extension 'docs_italia_theme' in the extensions list
extensions = [
  # ...,
  'docs_italia_theme'
]

# Edit these lines
html_theme = "docs_italia_theme"
html_theme_path = [docs_italia_theme.get_html_theme_path()]

master_doc = 'index'
numfig = True
numfig_secnum_depth = 0
