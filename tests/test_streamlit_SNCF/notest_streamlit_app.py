"""
Démo Streamlit — Affichage trains en retard
============================================================================

Pour lancer l'application :
    uv sync (lance le sync des dépendances)
    cd ./
    uv run streamlit run ./streamlit/streamlit_app.py

Le fichier `regularite-mensuelle-tgv-aqst.csv` doit contenir au minimum colonnes :
    "Gare de départ", "Retard moyen des trains en retard au départ"

"""

import logging

import streamlit as st
from test_back_end import test_load_data as ld
from test_front_end import test_graphes as ui
from test_front_end import test_sections as sc

# from utils.logger import init_logger

# test_init_logger()

logger = logging.getLogger(__name__)
logger.info("Application Streamlit démarrée")

# --------------------------------------------------------------------------
# Configuration générale de la page
# --------------------------------------------------------------------------

st.set_page_config(
    page_title="Démo - Retard moyen des trains d'une ville de départ",
    page_icon="🚄",
    layout="wide",
)

st.title("🚄 Démo - Retard moyen des trains d'une ville de départ")
st.caption(
    "Première base pour dérouler le workflow complet jusqu'au déploiement continu"
)

# --------------------------------------------------------------------------
# 1. Chargement des données
# --------------------------------------------------------------------------

df = sc.affichage_sidebar(ld.file_upload())

# --------------------------------------------------------------------------
# 2. Affichage données
# --------------------------------------------------------------------------

ui.liste_retards_moyens_france(df)
ui.hist_retard_ville_depart(df)
