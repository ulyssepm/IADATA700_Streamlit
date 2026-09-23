"""    
Module de fonctions front-end
"""

import pandas as pd
import streamlit as st

@st.cache_data # mémorise le résultat d’une fonction pour éviter de la recalculer à chaque interaction Streamlit.

def load_data(source: None) -> pd.DataFrame:
    """Charge un fichier csv, de séparateurs ";", utilisé pour l'analyse de données

    Args:
        source (None): input de type input = st.sidebar.file_uploader()

    Returns:
        pd.DataFrame: retourne le csv converti en DataFrame
    """
        
    df = pd.read_csv(source, sep=";")
    df = df[["Gare de départ","Retard moyen des trains en retard au départ"]]
    df = df.rename(
        columns={
            "Gare de départ": "GareDepart",
            "Retard moyen des trains en retard au départ": "RetMoyDepart",
        }
    )
    return df