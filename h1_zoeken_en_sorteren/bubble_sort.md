# Bubble sort

Implementeer het sorteeralgoritme "bubble sort" zoals gespecificeerd in de cursus als de methode  `bubble_sort`. 
Om te verifiëren of het sorteeralgoritme correct werd geïmplementeerd druk 
je de rij af na elke iteratie van de buitenste lus. Je kan hiervoor eenvoudigweg de opdracht
```
print(a)
```
gebruiken, waarbij `a` het argument is van de functie `bubble_sort`.
Tel eveneens hoe vaak het `if`-statement wordt *uitgevoerd*. Op het einde van 
je methode druk je de volgende lijn af.
```
Voor een rij van lengte <n> werd het if-statement <aantal> keer uitgevoerd
```
Kan je achterhalen wat de formule is voor `aantal` in functie van `n`. Wat zegt
dit over de tijdscomlexiteit van deze methode?


## Invoer
De invoer bestaat telkens uit één lijn gehele getallen, van elkaar gescheiden door een spatie. Deze lijn kan je als volgt inlezen en 
omzetten naar een lijst van gehele getallen.
```
a = [int(_) for _ in input().split()]
```

## Uitvoer

Alle rijen zoals afgedrukt tijdens de uitvoering van het algoritme.
Bv. wanneer de volgende rij wordt gegeven als invoer van het programma:
```
44 55 12 42 94 18 6 67
```
dan is de uitvoer
```
[6, 44, 55, 12, 42, 94, 18, 67]
[6, 12, 44, 55, 18, 42, 94, 67]
[6, 12, 18, 44, 55, 42, 67, 94]
[6, 12, 18, 42, 44, 55, 67, 94]
[6, 12, 18, 42, 44, 55, 67, 94]
[6, 12, 18, 42, 44, 55, 67, 94]
[6, 12, 18, 42, 44, 55, 67, 94]
Voor een rij van lengte 8 werd het if-statement 28 keer uitgevoerd
```
