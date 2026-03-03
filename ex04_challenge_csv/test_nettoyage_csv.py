"""
Tests pour le module nettoyage_csv.

Pour lancer les tests :
    python test_nettoyage_csv.py
ou
    python -m unittest test_nettoyage_csv.py
"""

import unittest
from nettoyage_csv import (
    supprimer_espaces_autour_separateurs,
    masquer_lignes_incompletes,
    valider_codes_postaux,
)


class TestSupprimerEspaces(unittest.TestCase):
    """Tests pour la fonction supprimer_espaces_autour_separateurs()."""

    def test_espaces_des_deux_cotes(self):
        self.assertEqual(
            supprimer_espaces_autour_separateurs("Martin ; Claire ; Mons ; 7000"),
            "Martin;Claire;Mons;7000",
        )

    def test_sans_espaces(self):
        ligne = "Dupont;Jean;Bruxelles;1000"
        self.assertEqual(supprimer_espaces_autour_separateurs(ligne), ligne)

    def test_espaces_multiples(self):
        self.assertEqual(
            supprimer_espaces_autour_separateurs("A  ;  B"),
            "A;B",
        )

    def test_espace_seulement_avant(self):
        self.assertEqual(
            supprimer_espaces_autour_separateurs("A ;B"),
            "A;B",
        )

    def test_espace_seulement_apres(self):
        self.assertEqual(
            supprimer_espaces_autour_separateurs("A; B"),
            "A;B",
        )

    # TODO: ajoutez un test avec des espaces à l'intérieur d'un champ
    #       (ex: "De Smet;Jan") --> les espaces internes ne doivent PAS être supprimés


class TestMasquerLignesIncompletes(unittest.TestCase):
    """Tests pour la fonction masquer_lignes_incompletes()."""

    def test_ligne_incomplete(self):
        self.assertEqual(
            masquer_lignes_incompletes(";;Liège;4000"),
            "[INCOMPLET] ;;Liège;4000",
        )

    def test_ligne_complete(self):
        ligne = "Dupont;Jean;Bruxelles;1000"
        self.assertEqual(masquer_lignes_incompletes(ligne), ligne)

    def test_champ_vide_au_milieu(self):
        self.assertEqual(
            masquer_lignes_incompletes("Dupont;;Bruxelles;1000"),
            "[INCOMPLET] Dupont;;Bruxelles;1000",
        )

    # TODO: ajoutez un test pour une ligne avec un champ vide en dernière position
    #       (ex: "Dupont;Jean;Bruxelles;")


class TestValiderCodesPostaux(unittest.TestCase):
    """Tests pour la fonction valider_codes_postaux()."""

    def test_code_postal_valide(self):
        ligne = "Dupont;Jean;Bruxelles;1000"
        self.assertEqual(valider_codes_postaux(ligne), ligne)

    def test_code_postal_invalide_lettres(self):
        self.assertEqual(
            valider_codes_postaux("Dupont;Jean;Bruxelles;ABC"),
            "Dupont;Jean;Bruxelles;????",
        )

    def test_code_postal_invalide_mixte(self):
        self.assertEqual(
            valider_codes_postaux("Dupont;Jean;Bruxelles;10OO"),
            "Dupont;Jean;Bruxelles;????",
        )

    def test_code_postal_cinq_chiffres(self):
        ligne = "Durand;Marie;Paris;75001"
        self.assertEqual(valider_codes_postaux(ligne), ligne)

    # TODO: ajoutez un test pour vérifier que les autres colonnes ne sont pas affectées
    #       même si elles contiennent des lettres


if __name__ == "__main__":
    unittest.main()
