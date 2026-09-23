# Utilisation de Sphinx

## `make.bat`

- `SOURCEDIR=.` indique que la racine Sphinx est le dossier `docs`.
- `BUILDDIR=_build` génère le résultat dans `docs/_build`.

## `conf.py`

Le dossier `../src` est ajouté au `sys.path` pour rendre le paquet
`streamlit_SNCF` importable :

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
```

L'extension `sphinx.ext.autodoc` est activée pour extraire les docstrings du
code Python :

```python
extensions = ["sphinx.ext.autodoc"]
```

## `index.rst`

La page `api` est ajoutée au `toctree` afin de l'intégrer à la documentation.

## `api.rst`

Cette page utilise les directives `automodule` et `:members:` pour documenter
les fonctions de `boutons.py` et `graphes.py`.

Sphinx lit ainsi sa configuration dans `docs`, importe le code depuis `src`,
puis génère les pages HTML dans `docs/_build/html`.