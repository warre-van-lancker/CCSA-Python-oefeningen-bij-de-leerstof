# Implementatie van gesloten hashing met lineaire peiling

Schrijf een klasse `HashSet` die een eenvoudige collectie implementeert m.b.v. gesloten hashing en lineaire peiling.

In het bijzonder moet deze klasse de volgende  methoden implementeren.

* `__init__(self, max_size=10)` initialiseert de collectie. De parameter `max_size` is het maximaal aantal elementen dat de collectie kan bevatten.
* `add(self, item)`. Voegt `item` toe aan de collectie. De returnwaarde is de index waar `item` werd toegevoegd. Wanneer de collectie "vol" is dan wordt een `ValueError` opgeworpen.
Om te verifiëren dat de implementatie correct werkt drukt de methode `add` alle gecontroleerde posities af op het standaarduitvoerkanaal. De finale positie wordt *niet* afgedrukt, m.a.w. als het algoritme bij de eerste poging een vrije plaats vindt dan wordt er niets afgedrukt.
 * `index_of(self, item)`. Retourneert de index waarop `item` zich bevindt, of `-1` wanneer `item` niet tot de collectie behoort. Om te verifiëren dat de implementatie correct werkt drukt deze methode eveneens alle gecontroleerde posities af, zoals voorheen besproken. 

Maak gebruik van de ingebouwde hashcode van Python om de hashcode van `item` te berekenen: `h = hash(item)`.

 

 Wanneer bovenstaande methoden geïmplementeerd zijn kan je de `HashSet` klasse uitbreiden
 met een methode `delete(self, item)` om elementen te verwijderen. Houd er rekening mee dat items niet zomaar 
 mogen worden verwijderd omdat er op die manier "gaten" zouden kunnen ontstaan in de sequenties die moeten doorzocht worden. Aan de andere kant moeten de posities waar elementen werden verwijderd wel weer kunnen worden ingenomen wanneer nieuwe elementen worden toegevoegd.
 De methode `delete` retourneert `True` wanneer `item` werd verwijderd, en `False` wanneer
 dit niet het geval is. Deze methode kan gebruikmaken van de methode `index_of` (en drukt
 bijgevolg ook een aantal posities af).


