"""Initialisation logger"""

import logging
from logging.handlers import (
    RotatingFileHandler,
)


def init_logger() -> None:
    """Initialisation du logger"""
    logger = logging.getLogger(__name__)
    logger.basicConfig(level=logging.INFO)  # INFO est le niveau par défaut
    # Handler pour écrire les logs dans un fichier
    # file_handler = logging.FileHandler("/logs/app.log")
    file_handler = RotatingFileHandler(
        "/logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=5
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


logger = init_logger()
