"""
Module spoilers - Censure de spoilers dans des messages de forum.

Les spoilers sont délimités par [spoiler]...[/spoiler].
"""

import re


def censurer_spoilers(message: str) -> str:
    """
    Remplace chaque bloc [spoiler]...[/spoiler] par [CENSURÉ].

    Chaque spoiler doit être remplacé indépendamment.

    Args:
        message (str): Le message contenant potentiellement des spoilers

    Returns:
        str: Le message avec les spoilers censurés

    Exemples:
        >>> censurer_spoilers("Il meurt à la fin [spoiler]le héros tombe[/spoiler] !")
        'Il meurt à la fin [CENSURÉ] !'
    """
    # TODO: utilisez re.sub() avec le bon quantificateur
    pass


def extraire_spoilers(message: str) -> list:
    """
    Extrait le contenu de tous les blocs [spoiler]...[/spoiler].

    Args:
        message (str): Le message à analyser

    Returns:
        list: Liste des textes cachés (sans les balises)

    Exemples:
        >>> extraire_spoilers("A [spoiler]secret1[/spoiler] et [spoiler]secret2[/spoiler]")
        ['secret1', 'secret2']
    """
    # TODO: utilisez re.findall() avec un groupe de capture
    pass
