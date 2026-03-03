# Exercice 1 - Extraction de mentions dans des messages

**Niveau :** Facile
**Temps estimé :** 15 minutes
**Concepts :** groupes de capture `()`, `match.groups()`, `re.findall()`

## Contexte

Dans un système de messagerie, les utilisateurs mentionnent d'autres personnes
avec le format `@prenom.nom`. On veut extraire séparément le prénom et le nom
de chaque mention.

## Instructions

1. Ouvrez `mentions.py`
2. Implémentez `decomposer_mention()` : reçoit une mention isolée comme
   `"@jean.dupont"` et retourne le prénom et le nom séparément
3. Implémentez `extraire_mentions()` : reçoit un message complet et retourne
   la liste de toutes les mentions trouvées sous forme de tuples `(prenom, nom)`
4. Lancez les tests : `python test_mentions.py`

## Critères de réussite

- [ ] `decomposer_mention("@jean.dupont")` retourne `("jean", "dupont")`
- [ ] `decomposer_mention("bonjour")` retourne `None`
- [ ] `extraire_mentions("Salut @ana.martin et @lou.bernard !")` retourne `[("ana", "martin"), ("lou", "bernard")]`
- [ ] `extraire_mentions("Pas de mention ici.")` retourne `[]`
- [ ] Tous les tests passent

## Indices

- Un prénom ou nom ne contient que des lettres minuscules (`[a-z]+`)
- `re.findall()` avec des groupes retourne directement une liste de tuples
