"""Ce module n'a pas a etre teste car il input un df issu d'un module streamlit deja fonctionnel"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# data_test = (
#     Path(__file__).resolve().parents[3]
#     / "data"
#     / "raw"
#     / "regularite-mensuelle-tgv-aqst.csv"
# )

# data_test_wrong_cols = (
#     Path(__file__).resolve().parents[3]
#     / "data"
#     / "raw"
#     / "regularite-mensuelle-intercites.csv"
# )


# def test_liste_retards_moyens_france_df():
#     assert isinstance(liste_retards_moyens_france(data_test), pd.DataFrame)

# def test_liste_retards_moyens_france_wrong():
#     assert isinstance(liste_retards_moyens_france(data_test_wrong_cols), pd.DataFrame)


def liste_retards_moyens_france(df: pd.Dataframe) -> None:
    """Affiche la liste complète des retards moyens
    au départ de toutes les gares de France"""

    gares = sorted(list(df["GareDepart"].unique()))
    RetMoy = [df.loc[df["GareDepart"] == gare]["RetMoyDepart"].mean() for gare in gares]
    df2 = pd.DataFrame(np.array([gares, RetMoy]).T, columns=["GareDepart", "RetMoy"])

    st.subheader("📋 Retards au départ moyens par ville de départ")
    st.dataframe(df2, use_container_width=True, hide_index=True)

    st.caption("Retards moyens")


def hist_retard_ville_depart(df: pd.DataFrame) -> None:
    """Affiche l'histogramme des retards moyens
    au départ d'une ville de départ sélectionnée"""

    st.subheader("📋 Histogrammes retards au départ par ville de départ")

    gares = sorted(list(df["GareDepart"].unique()))
    ville_depart = st.selectbox(
        "Ville de départ :",
        gares,
    )

    fig, ax = plt.subplots()
    df_RetMoyDepart = df.loc[df["GareDepart"] == ville_depart]["RetMoyDepart"]
    ax.hist(df_RetMoyDepart)
    ax.plot(
        pd.DataFrame(
            data=np.ones(np.shape(df_RetMoyDepart)[0])
            * df.loc[df["GareDepart"] == ville_depart]["RetMoyDepart"].mean()
        )
    )
    ax.plot(
        pd.DataFrame(
            data=np.ones(np.shape(df_RetMoyDepart)[0]) * df["RetMoyDepart"].mean()
        )
    )
    ax.legend(["Retard moyen ville", "Retard moyen France", "Retards ville"])
    ax.set_ylabel("Nombre de trains (#)")
    ax.set_xlabel("Retard moyen au départ (mn)")
    st.pyplot(fig)
    # st.area_chart(df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"])
    # st.line_chart(pd.DataFrame(data=np.ones(np.shape(df)[0])*df.loc[df["GareDepart"]==ville_depart]["RetMoyDepart"].mean()))
