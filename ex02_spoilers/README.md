# Exercice 2 - Censure de spoilers dans un forum

**Niveau :** Moyen
**Temps estimé :** 15 minutes
**Concepts :** greedy vs lazy (`*` vs `*?`), `re.sub()`, backreferences `\1`

## Contexte

Sur un forum de cinéma, les utilisateurs marquent les spoilers entre
balises `[spoiler]...[/spoiler]`. On veut remplacer le contenu des spoilers
par `[CENSURÉ]` tout en gardant le reste du message intact.

## Instructions

1. Ouvrez `spoilers.py`
2. Implémentez `censurer_spoilers()` : remplace chaque bloc
   `[spoiler]...[/spoiler]` par `[CENSURÉ]`
3. Implémentez `extraire_spoilers()` : retourne la liste des textes cachés
   dans les balises spoiler
4. Lancez les tests : `python test_spoilers.py`

## Critères de réussite

- [ ] Un message avec un spoiler est correctement censuré
- [ ] Un message avec **deux** spoilers les censure **indépendamment** (pas tout d'un bloc !)
- [ ] Un message sans spoiler reste inchangé
- [ ] `extraire_spoilers()` retourne la liste des contenus cachés
- [ ] Tous les tests passent

## Piège à éviter

Réfléchissez à ce qui se passe quand un message contient **deux** blocs spoiler.
Que se passe-t-il si votre quantificateur est trop gourmand ?
