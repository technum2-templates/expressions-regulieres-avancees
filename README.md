# Exercices - Expressions régulières avancées

Exercices de pratique sur les concepts avancés des expressions régulières en Python.

## Liste des exercices

| #  | Dossier              | Niveau    | Temps  | Concepts principaux                                   |
|----|----------------------|-----------|--------|-------------------------------------------------------|
| 01 | `ex01_mentions`      | Facile    | 15 min | Groupes de capture `()`, `re.findall()` avec groupes  |
| 02 | `ex02_spoilers`      | Moyen     | 15 min | Greedy vs lazy (`*` vs `*?`), `re.sub()`              |
| 03 | `ex03_montants`      | Moyen     | 20 min | Alternatives `\|`, groupes non capturants `(?:...)`   |
| 04 | `ex04_challenge_csv` | Difficile | 25 min | Lookahead, lookbehind, combinaison de tout             |

## Prérequis

- Avoir suivi la partie théorique sur les expressions régulières avancées
- Connaître `re.match()`, `re.search()`, `re.findall()`, `re.sub()`

## Lancer les tests

Depuis le dossier d'un exercice :

```bash
python test_<module>.py
```

## Conseils

- Testez vos patterns sur [regex101.com](https://regex101.com) (flavour Python) avant de coder
- Lisez bien les docstrings et les exemples dans le code
- Les TODO dans les fichiers de test vous invitent à ajouter vos propres cas de test
- L'exercice 4 est un **challenge** : ne le commencez que si vous avez terminé les trois premiers
