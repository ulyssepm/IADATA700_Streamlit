"""Module de fonctions de chargement de données"""

import pandas as pd
import streamlit as st


@st.cache_data  # mémorise le résultat d’une fonction pour éviter de la recalculer à
# chaque interaction Streamlit.

def load_data(source: str) -> pd.DataFrame:
    """Charge un fichier csv, de séparateurs ";", utilisé pour l'analyse de données

    Args:
        source (str): input de type input = st.sidebar.file_uploader()

    Returns:
        df (pd.DataFrame): retourne le csv converti en DataFrame
    """

    df = pd.read_csv(source, sep=";")
    df = df[["Gare de départ", "Retard moyen des trains en retard au départ"]]
    df = df.rename(
        columns={
            "Gare de départ": "GareDepart",
            "Retard moyen des trains en retard au départ": "RetMoyDepart",
        }
    )
    return df


def file_upload() -> pd.Dataframe:
    """Affiche la barre latérale avec les modules choisis

    Returns:
        pd.Dataframe: le dataframe contenant les données importées
    """

    file_uploader = st.sidebar.file_uploader(
        "Charger un CSV (colonnes: Gares, Retards ...)", type=["csv"]
    )

    # Si l'utilisateur ne charge rien, on utilise le CSV d'exemple fourni
    if file_uploader is not None:
        df = load_data(file_uploader)
    else:
        df = load_data("data/raw/regularite-mensuelle-tgv-aqst.csv")
        st.sidebar.info(
            "Aucun fichier chargé : utilisation de `regularite-mensuelle-tgv-aqst.csv`."
        )

    st.sidebar.write(f"**{len(df)}** données chargées")

    return df
