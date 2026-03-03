# Exercice 3 - Extraction de montants dans un rapport financier

**Niveau :** Moyen
**Temps estimé :** 20 minutes
**Concepts :** alternatives `|`, groupes non capturants `(?:...)`, `re.findall()`

## Contexte

Un rapport financier contient des montants exprimés en différentes devises.
On veut extraire ces montants et normaliser leur format.

Les formats possibles sont :

- `150 EUR` ou `150 USD` ou `150 GBP` (nombre + espace + devise)
- `€150` ou `$150` ou `£150` (symbole collé avant le nombre)

Les nombres peuvent contenir des décimales : `12.50`, `1499.99`

## Instructions

1. Ouvrez `montants.py`
2. Implémentez `extraire_montants()` : retourne la liste de tous les montants
   trouvés dans un texte, chacun sous forme de tuple `(nombre, devise)`
3. Implémentez `total_par_devise()` : retourne un dictionnaire avec le total
   par devise
4. Lancez les tests : `python test_montants.py`

## Critères de réussite

- [ ] `"Facture : 150 EUR"` retourne `[("150", "EUR")]`
- [ ] `"Coût : €49.99"` retourne `[("49.99", "EUR")]`
- [ ] Les symboles `€`, `$`, `£` sont convertis en `EUR`, `USD`, `GBP`
- [ ] Un texte sans montant retourne `[]`
- [ ] Tous les tests passent

## Indices

- Vous aurez besoin de **deux patterns** (ou d'un seul avec des alternatives)
  pour gérer les deux formats
- `(?:...)` est utile pour grouper des alternatives sans polluer les groupes
  de capture
- Réfléchissez à ce que `re.findall()` retourne quand le pattern contient
  des groupes de capture
