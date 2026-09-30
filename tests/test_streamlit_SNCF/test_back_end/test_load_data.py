"""Module de fonctions de chargement de données"""

from pathlib import Path

import pandas as pd
import pytest

from streamlit_SNCF.back_end import load_data as ld

data_test = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "raw"
    / "regularite-mensuelle-tgv-aqst.csv"
)

data_test_png = (
    Path(__file__).resolve().parents[3] / "data" / "processed" / "pairplot.png"
)


def test_load_data() -> None:
    assert isinstance(ld.load_data(data_test), pd.DataFrame)


def test_load_png():
    with pytest.raises(ValueError):
        ld.load_data(data_test_png)


def test_load_int():
    with pytest.raises(ValueError):
        ld.load_data(42)
