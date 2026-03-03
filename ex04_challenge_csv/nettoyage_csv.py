"""
Module nettoyage_csv - Nettoyage de données CSV avec des regex avancées.

Format attendu : colonnes séparées par des points-virgules (;)
    nom;prenom;ville;code_postal
"""

import re


def supprimer_espaces_autour_separateurs(ligne: str) -> str:
    """
    Supprime les espaces superflus avant et après les points-virgules.

    Args:
        ligne (str): Une ligne CSV

    Returns:
        str: La ligne nettoyée

    Exemples:
        >>> supprimer_espaces_autour_separateurs("Martin ; Claire ; Mons ; 7000")
        'Martin;Claire;Mons;7000'
        >>> supprimer_espaces_autour_separateurs("Dupont;Jean;Bruxelles;1000")
        'Dupont;Jean;Bruxelles;1000'
    """
    # TODO: utilisez re.sub() avec lookahead et/ou lookbehind pour cibler
    # les espaces qui sont juste avant ou juste après un point-virgule
    pass


def masquer_lignes_incompletes(ligne: str) -> str:
    """
    Préfixe la ligne par "[INCOMPLET] " si elle contient un champ vide
    (deux points-virgules consécutifs).

    Si la ligne est complète, elle est retournée telle quelle.

    Args:
        ligne (str): Une ligne CSV

    Returns:
        str: La ligne éventuellement préfixée

    Exemples:
        >>> masquer_lignes_incompletes(";;Liège;4000")
        '[INCOMPLET] ;;Liège;4000'
        >>> masquer_lignes_incompletes("Dupont;Jean;Bruxelles;1000")
        'Dupont;Jean;Bruxelles;1000'
    """
    # TODO: utilisez re.search() pour détecter deux ; consécutifs
    pass


def valider_codes_postaux(ligne: str) -> str:
    """
    Remplace le code postal (dernière colonne) par "????" s'il ne contient
    pas uniquement des chiffres.

    Le code postal est la partie après le dernier point-virgule.

    Args:
        ligne (str): Une ligne CSV

    Returns:
        str: La ligne avec le code postal corrigé si nécessaire

    Exemples:
        >>> valider_codes_postaux("Dupont;Jean;Bruxelles;ABC")
        'Dupont;Jean;Bruxelles;????'
        >>> valider_codes_postaux("Dupont;Jean;Bruxelles;1000")
        'Dupont;Jean;Bruxelles;1000'
    """
    # TODO: utilisez re.sub() avec un lookbehind pour cibler la dernière
    # colonne et vérifier si elle contient des caractères non numériques
    pass
