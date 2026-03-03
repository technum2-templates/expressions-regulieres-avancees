"""
Tests pour le module montants.

Pour lancer les tests :
    python test_montants.py
ou
    python -m unittest test_montants.py
"""

import unittest
from montants import extraire_montants, total_par_devise


class TestExtraireMontants(unittest.TestCase):
    """Tests pour la fonction extraire_montants()."""

    def test_format_code_devise(self):
        self.assertEqual(extraire_montants("Total : 150 EUR"), [("150", "EUR")])

    def test_format_symbole(self):
        self.assertEqual(extraire_montants("Prix : €49.99"), [("49.99", "EUR")])

    def test_dollar(self):
        self.assertEqual(extraire_montants("Cost: $120"), [("120", "USD")])

    def test_livre_sterling(self):
        self.assertEqual(extraire_montants("Price: £75.50"), [("75.50", "GBP")])

    def test_plusieurs_montants_mixtes(self):
        texte = "Revenus : 500 EUR, dépenses : $200 et £30.50"
        resultat = extraire_montants(texte)
        self.assertIn(("500", "EUR"), resultat)
        self.assertIn(("200", "USD"), resultat)
        self.assertIn(("30.50", "GBP"), resultat)

    def test_aucun_montant(self):
        self.assertEqual(extraire_montants("Pas de montant ici."), [])

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Un montant avec des décimales dans le format code (ex: "99.99 USD")
    # - Un nombre seul sans devise (ex: "Il y a 42 étudiants") --> ne doit PAS matcher


class TestTotalParDevise(unittest.TestCase):
    """Tests pour la fonction total_par_devise()."""

    def test_une_seule_devise(self):
        self.assertEqual(total_par_devise("100 EUR et €50"), {"EUR": 150.0})

    def test_plusieurs_devises(self):
        resultat = total_par_devise("100 EUR et $50 et £25")
        self.assertAlmostEqual(resultat["EUR"], 100.0)
        self.assertAlmostEqual(resultat["USD"], 50.0)
        self.assertAlmostEqual(resultat["GBP"], 25.0)

    def test_texte_sans_montant(self):
        self.assertEqual(total_par_devise("Rien du tout"), {})

    # TODO: ajoutez un test avec des montants décimaux dans plusieurs devises


if __name__ == "__main__":
    unittest.main()
