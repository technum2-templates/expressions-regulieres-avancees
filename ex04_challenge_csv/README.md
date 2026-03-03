# Exercice 4 (Challenge) - Nettoyage intelligent de données CSV

**Niveau :** Difficile
**Temps estimé :** 25 minutes
**Concepts :** lookahead `(?=...)`, lookbehind `(?<=...)`, lookahead négatif `(?!...)`, `re.sub()`, combinaison de tous les concepts

## Contexte

Vous recevez des données CSV mal formatées qu'il faut nettoyer avant import.
Les problèmes sont multiples et chaque fonction de nettoyage cible un souci
précis, en utilisant les regex avancées.

## Les données

```text
nom;prenom;ville;code_postal
Dupont;Jean;Bruxelles;1000
Martin ; Claire ; Mons ; 7000
;;Liège;4000
Bernard;  Luc  ;Namur;5000
Dupont;Jean;Bruxelles;ABC
```

## Instructions

1. Ouvrez `nettoyage_csv.py`
2. Implémentez les 3 fonctions de nettoyage :
   - `supprimer_espaces_autour_separateurs()` : supprime les espaces avant
     et après les `;` (lookbehind/lookahead)
   - `masquer_lignes_incompletes()` : marque les lignes qui ont des champs
     vides (deux `;` consécutifs) en ajoutant `[INCOMPLET] ` au début
   - `valider_codes_postaux()` : remplace les codes postaux non numériques
     par `????` (lookbehind + négation)
3. Lancez les tests : `python test_nettoyage_csv.py`

## Critères de réussite

- [ ] `" ; "` devient `";"` (espaces supprimés autour du séparateur)
- [ ] `"a;b"` reste `"a;b"` (pas d'espace = pas de changement)
- [ ] Les lignes avec `;;` sont préfixées par `[INCOMPLET] `
- [ ] Un code postal `ABC` en dernière colonne est remplacé par `????`
- [ ] Un code postal `1000` reste intact
- [ ] Tous les tests passent

## Indices

- `(?<=;)` signifie "précédé d'un point-virgule"
- `(?=;)` signifie "suivi d'un point-virgule"
- Pour les espaces autour des `;`, pensez à deux substitutions séparées
  (ou une seule regex plus avancée)
- Pour le code postal, il est toujours en fin de ligne : pensez à `$`
