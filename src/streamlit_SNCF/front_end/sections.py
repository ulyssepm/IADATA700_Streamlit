
"""
Module d'affichages de sections du site web
"""

import pandas as pd
import streamlit as st
from front_end import boutons as bt

def affichageSidebar() -> pd.Dataframe:
    """Affiche la barre latérale avec les modules choisis

    Returns:
        pd.Dataframe: le dataframe contenant les données importées
    """
    
    st.sidebar.header("⚙️ Paramètres")

    file_uploader = st.sidebar.file_uploader(
        "Charger un CSV (colonnes: Gares, Retards ...)", type=["csv"]
    )

    #

    # Si l'utilisateur ne charge rien, on utilise le CSV d'exemple fourni
    if file_uploader is not None:
        df = bt.load_data(file_uploader)
    else:
        df = bt.load_data("data/raw/regularite-mensuelle-tgv-aqst.csv")
        st.sidebar.info(
            "Aucun fichier chargé : utilisation de "
            "`regularite-mensuelle-tgv-aqst.csv`."
        )

    st.sidebar.write(f"**{len(df)}** données chargées")
    
    return df