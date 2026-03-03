"""
Module montants - Extraction de montants financiers dans un texte.

Formats reconnus :
    - 150 EUR, 49.99 USD, 12 GBP       (nombre + espace + code devise)
    - €150, $49.99, £12                  (symbole + nombre)
"""

import re

# Correspondance entre symboles et codes devises
SYMBOLES = {
    "€": "EUR",
    "$": "USD",
    "£": "GBP",
}


def extraire_montants(texte: str) -> list:
    """
    Extrait tous les montants d'un texte.

    Chaque montant est retourné sous forme de tuple (nombre, devise)
    où devise est toujours le code à 3 lettres (EUR, USD, GBP).

    Args:
        texte (str): Le texte à analyser

    Returns:
        list: Liste de tuples (nombre, devise)

    Exemples:
        >>> extraire_montants("Facture : 150 EUR et €49.99")
        [('150', 'EUR'), ('49.99', 'EUR')]
        >>> extraire_montants("Rien à signaler.")
        []
    """
    # TODO: trouvez les montants dans les deux formats et normalisez les devises
    # Conseil : vous pouvez utiliser deux re.findall() séparés, ou un seul
    # pattern plus avancé avec des alternatives.
    pass


def total_par_devise(texte: str) -> dict:
    """
    Calcule le total des montants par devise.

    Args:
        texte (str): Le texte à analyser

    Returns:
        dict: Dictionnaire {devise: total} (ex: {"EUR": 199.99, "USD": 50.0})

    Exemples:
        >>> total_par_devise("Dépenses : 100 EUR et €49.99 puis $25")
        {'EUR': 149.99, 'USD': 25.0}
    """
    # TODO: utilisez extraire_montants() et agrégez les résultats
    pass
