"""
Démo Streamlit — Affichage cartographique avec pydeck (fond OpenStreetMap)
============================================================================

Pour lancer l'application :
    #pip install -r requirements.txt
    uv sync (lance le sync des dépendances)
    cd ./
    streamlit run ./streamlit/streamlit_app.py

Le fichier `donnees.csv` doit contenir au minimum deux colonnes :
    latitude, longitude
(des colonnes supplémentaires comme "nom" ou "valeur" sont optionnelles
et utilisées ici pour la couleur/taille des points et les infobulles).
"""

import pandas as pd
import pydeck as pdk
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Configuration générale de la page
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Démo carto — pydeck + OpenStreetMap",
    page_icon="🗺️",
    layout="wide",
)

st.title("🗺️ Démo — Carte de données avec pydeck sur fond OpenStreetMap")
st.caption("Exemple pédagogique pour un cours de Python en production (Streamlit)")

# --------------------------------------------------------------------------
# 1. Chargement des données
# --------------------------------------------------------------------------
st.sidebar.header("⚙️ Paramètres")

file_uploader = st.sidebar.file_uploader(
    "Charger un CSV (colonnes: latitude, longitude, ...)", type=["csv"]
)


@st.cache_data
def load_data(source) -> pd.DataFrame:
    """Charge un CSV et extraie, renomme les colonnes
    df = pd.read_csv(source)
    df.columns = [c.strip().lower() for c in df.columns]
    if "latitude" not in df.columns or "longitude" not in df.columns:
        raise ValueError("Le CSV doit contenir des colonnes 'latitude' et 'longitude'.")
    """
        
    df = pd.read_csv("streamlit_SNCF/regularite-mensuelle-tgv-aqst.csv", sep=";")
    df = df[["Gare de départ","Retard moyen des trains en retard au départ"]]
    df = df.rename(
        columns={
            "Gare de départ": "GareDepart",
            "Retard moyen des trains en retard au départ": "RetMoyDepart",
        }
    )
    return df


# Si l'utilisateur ne charge rien, on utilise le CSV d'exemple fourni
if file_uploader is not None:
    df = load_data(file_uploader)
else:
    df = load_data("streamlit_SNCF/regularite-mensuelle-tgv-aqst.csv")
    st.sidebar.info("Aucun fichier chargé : utilisation de `regularite-mensuelle-tgv-aqst.csv` (exemple).")

st.sidebar.write(f"**{len(df)}** données chargées")


# --------------------------------------------------------------------------
# 7. Affichage données
# --------------------------------------------------------------------------

######### Liste globale ############
st.subheader("📋 Données brutes retards par gare de départ")
st.dataframe(df_filtered, use_container_width=True, hide_index=True)

st.caption(
    "Fond de carte : © contributeurs OpenStreetMap — tuiles servies via TileLayer pydeck."
)

######### Liste retards moyens par ville de départ ############

#df2 = df[["Gare de départ","Retard moyen des trains en retard au départ"]]
#df2 = df2.rename(columns={"Gare de départ": "GareDepart", "Retard moyen des trains en retard au départ": "RetMoyDepart"})

gares=sorted(list(df["GareDepart"].unique()))
RetMoy=[df.loc[df["GareDepart"]==gare]["RetMoyDepart"].mean() for gare in gares]
df2 = pd.DataFrame(np.array([gares,RetMoy]).T, columns=["GareDepart","RetMoy"])

st.subheader("📋 Retards au départ moyens par ville de départ")
st.dataframe(df2, use_container_width=True, hide_index=True)

st.caption(
    "Fond de carte : © contributeurs OpenStreetMap — tuiles servies via TileLayer pydeck."
)

######### Histogramme retards par ville sélectionnée ############
st.subheader("📋 Histogrammes retards au départ par ville de départ")

ville_depart = st.selectbox(
    "Ville de départ :",
    gares,
)

fig, ax = plt.subplots()
df_RetMoyDepart = df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"]
ax.hist(df_RetMoyDepart)
ax.plot(pd.DataFrame(data=np.ones(np.shape(df_RetMoyDepart)[0])*df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"].mean()))
ax.plot(pd.DataFrame(data=np.ones(np.shape(df_RetMoyDepart)[0])*df["RetMoyDepart"].mean()))
ax.legend(['Retard moyen ville','Retard moyen France', 'Retards ville'])
st.pyplot(fig)
#st.area_chart(df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"])
#st.line_chart(pd.DataFrame(data=np.ones(np.shape(df)[0])*df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"].mean()))