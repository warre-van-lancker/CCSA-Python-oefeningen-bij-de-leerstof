# Stapel met gelinkte lijst

Schrijf een klasse `StackList` die een stapel implementeert m.b.v. een gelinkte lijst. 
De klasse `StackList` moet over de volgende methoden beschikken.
* `StackList`: de constructor
* `is_empty`: controleert of de stapel leeg is
* `push`: plaatst een element boven op de stapel
* `peek`: bekijkt het bovenste element van de stapel
* `pop`: retourneert en verwijdert het bovenste element van de stapel.

Een mogelijk gebruik van deze stapel is als volgt:

```
>>> s = StackList()
>>> s.is_empty()
True
>>> s.push("This")
>>> s.is_empty()
False
>>> s.peek()
'This'
>>> s.push("Is")
>>> s.push("A Test")
>>> s.peek()
'A Test'
>>> s.pop()
'A Test'
>>> s.pop()
'Is'
>>> s.is_empty()
False
>>> s.pop()
'This'
>>> s.is_empty()
True
```
