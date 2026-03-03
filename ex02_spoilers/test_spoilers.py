"""
Tests pour le module spoilers.

Pour lancer les tests :
    python test_spoilers.py
ou
    python -m unittest test_spoilers.py
"""

import unittest
from spoilers import censurer_spoilers, extraire_spoilers


class TestCensurerSpoilers(unittest.TestCase):
    """Tests pour la fonction censurer_spoilers()."""

    def test_un_spoiler(self):
        message = "Il découvre que [spoiler]Dark Vador est son père[/spoiler] à la fin."
        attendu = "Il découvre que [CENSURÉ] à la fin."
        self.assertEqual(censurer_spoilers(message), attendu)

    def test_deux_spoilers_independants(self):
        message = "A: [spoiler]secret A[/spoiler] et B: [spoiler]secret B[/spoiler]."
        attendu = "A: [CENSURÉ] et B: [CENSURÉ]."
        self.assertEqual(censurer_spoilers(message), attendu)

    def test_message_sans_spoiler(self):
        message = "Ce film est génial, aucun spoiler ici."
        self.assertEqual(censurer_spoilers(message), message)

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Un spoiler qui contient des caractères spéciaux (ex: "100% de chances")
    # - Un message qui ne contient QUE le spoiler (pas de texte autour)


class TestExtraireSpoilers(unittest.TestCase):
    """Tests pour la fonction extraire_spoilers()."""

    def test_deux_spoilers(self):
        message = "A [spoiler]secret1[/spoiler] et [spoiler]secret2[/spoiler]"
        self.assertEqual(extraire_spoilers(message), ["secret1", "secret2"])

    def test_aucun_spoiler(self):
        self.assertEqual(extraire_spoilers("Rien à cacher."), [])

    def test_un_spoiler(self):
        message = "Attention [spoiler]il survit[/spoiler] ouf."
        self.assertEqual(extraire_spoilers(message), ["il survit"])

    # TODO: ajoutez un test supplémentaire de votre choix


if __name__ == "__main__":
    unittest.main()
