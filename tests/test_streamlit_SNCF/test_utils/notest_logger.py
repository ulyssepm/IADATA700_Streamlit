"""Initialisation logger"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"


def init_logger() -> logging.Logger:
    """Initialisation du logger"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # Handler pour écrire les logs dans un fichier

    # évite d'ajouter les handlers en double à chaque rerun de Streamlit
    if logger.handlers:
        return logger

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        LOG_DIR / "app.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )  # celui-ci permet de limiter la taille des fichiers
    file_handler.setLevel(
        logging.ERROR
    )  # Ne log que les erreurs et les messages plus critiques
    # Handler pour afficher les logs dans la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Affiche tous les niveaux de logs
    # Ajout des handlers au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False
    return logger


logger = init_logger()
