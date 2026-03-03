"""
Tests pour le module mentions.

Pour lancer les tests :
    python test_mentions.py
ou
    python -m unittest test_mentions.py
"""

import unittest
from mentions import decomposer_mention, extraire_mentions


class TestDecomposerMention(unittest.TestCase):
    """Tests pour la fonction decomposer_mention()."""

    def test_mention_valide(self):
        self.assertEqual(decomposer_mention("@jean.dupont"), ("jean", "dupont"))

    def test_mention_invalide_sans_arobase(self):
        self.assertIsNone(decomposer_mention("jean.dupont"))

    def test_mention_invalide_texte_quelconque(self):
        self.assertIsNone(decomposer_mention("bonjour"))

    def test_mention_invalide_sans_point(self):
        self.assertIsNone(decomposer_mention("@jeandupont"))

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Une mention avec des majuscules (ex: "@Jean.Dupont") --> invalide
    # - Une chaîne vide


class TestExtraireMentions(unittest.TestCase):
    """Tests pour la fonction extraire_mentions()."""

    def test_message_avec_deux_mentions(self):
        resultat = extraire_mentions("Salut @ana.martin et @lou.bernard !")
        self.assertEqual(resultat, [("ana", "martin"), ("lou", "bernard")])

    def test_message_sans_mention(self):
        self.assertEqual(extraire_mentions("Pas de mention ici."), [])

    def test_message_avec_une_mention(self):
        self.assertEqual(
            extraire_mentions("Bravo @sam.petit pour le travail !"),
            [("sam", "petit")],
        )

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Un message avec une mention en début de ligne
    # - Un message contenant un email (ex: "sam.petit@mail.com") --> ne doit PAS matcher


if __name__ == "__main__":
    unittest.main()
