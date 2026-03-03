"""
Module mentions - Extraction de mentions @prenom.nom dans des messages.
"""

import re


def decomposer_mention(texte: str) -> tuple | None:
    """
    Décompose une mention au format @prenom.nom en ses parties.

    La chaîne doit correspondre exactement à une mention (pas de texte autour).

    Args:
        texte (str): La chaîne à analyser

    Returns:
        tuple | None: Un tuple (prenom, nom) ou None si le format est invalide

    Exemples:
        >>> decomposer_mention("@jean.dupont")
        ('jean', 'dupont')
        >>> decomposer_mention("bonjour")
        None
    """
    # TODO: utilisez re.match() avec des groupes de capture
    pass


def extraire_mentions(message: str) -> list:
    """
    Trouve toutes les mentions @prenom.nom dans un message.

    Args:
        message (str): Le message à analyser

    Returns:
        list: Liste de tuples (prenom, nom) pour chaque mention trouvée

    Exemples:
        >>> extraire_mentions("Salut @ana.martin et @lou.bernard !")
        [('ana', 'martin'), ('lou', 'bernard')]
        >>> extraire_mentions("Pas de mention ici.")
        []
    """
    # TODO: utilisez re.findall() avec des groupes de capture
    pass
