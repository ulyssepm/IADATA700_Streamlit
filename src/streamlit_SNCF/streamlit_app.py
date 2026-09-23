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
from affichage_donnee import graphes as ui
from front_end import sections as sc
from utils.logger import init_logger

init_logger()

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

df = sc.affichageSidebar()

# --------------------------------------------------------------------------
# 2. Affichage données
# --------------------------------------------------------------------------

ui.listeRetardsMoyensFrance(df)
ui.histRetardVilleDepart(df)
