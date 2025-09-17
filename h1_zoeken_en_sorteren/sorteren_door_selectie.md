# Sorteren door selectie

Herwerk de oplossingsmethode voor sorteren door selectie zodat niet
langer het grootste element naar achteren wordt gebracht maar het
kleinste element naar voor. Het reeds gesorteerde deel van de array
bevindt zich m.a.w. steeds vooraan.

Om te kunnen verifiëren dat de sortering op de correcte manier gebeurt
druk je de lijst af na elke iteratie van de buitenste lus.

Schrijf een functie `selection_sort_vooraan` en roep deze aan.

### Invoer

De invoer bestaat telkens uit één lijn gehele getallen, van elkaar gescheiden door een spatie. Deze lijn kan je als volgt inlezen en 
omzetten naar een lijst van gehele getallen.
```
a = [int(_) for _ in input().split()]
```

### Uitvoer

Je programma drukt een aantal lijnen af. Elke lijn is het gevolg 
van een `print` opdracht op het einde van de buitenste lus, dus net
nadat twee elementen van plaats werden gewisseld in de lijst.
Je kan hiervoor eenvoudigweg de opdracht
```
print(a)
```
gebruiken, waarbij `a` het argument is van de functie `selection_sort_vooraan`.


**Invoer:**

    44 55 12 42 94 18 6 67


**Uitvoer:**

    [6, 55, 12, 42, 94, 18, 44, 67]
    [6, 12, 55, 42, 94, 18, 44, 67]
    [6, 12, 18, 42, 94, 55, 44, 67]
    [6, 12, 18, 42, 94, 55, 44, 67]
    [6, 12, 18, 42, 44, 55, 94, 67]
    [6, 12, 18, 42, 44, 55, 94, 67]
    [6, 12, 18, 42, 44, 55, 67, 94]




