"""Module d'affichages de sections du site web"""

import pandas as pd
import streamlit as st


def affichage_sidebar(widget: None) -> pd.Dataframe:
    """Affiche la barre latérale avec les widgets choisis

    Returns:
        pd.Dataframe: le dataframe contenant les données importées
    """

    st.sidebar.header("⚙️ Paramètres")

    # Liste widgets à insérer

    df = widget

    return df
