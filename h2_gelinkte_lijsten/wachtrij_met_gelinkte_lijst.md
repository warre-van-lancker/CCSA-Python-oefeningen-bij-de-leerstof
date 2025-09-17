# Wachtrij met gelinkte lijst

Schrijf een klasse `QueueList` die een wachtrij implementeert m.b.v. een gelinkte lijst. 
De klasse `QueueList` moet over de volgende methoden beschikken.
* `QueueList`: de constructor
* `is_empty`: controleert of de stapel leeg is
* `enqueue`: voegt een element toe achteraan aan de wachtrij
* `front`: bekijkt het eerste element van de wachtrij
* `dequeue`: retourneert en verwijdert het voorste element van de wachtrij

Een mogelijk gebruik van deze wachtrij is als volgt:

```
>>> q = QueueList()
>>> q.is_empty()
True
>>> q.enqueue("One")
>>> q.is_empty()
False
>>> q.front()
'One'
>>> q.enqueue("Two")
>>> q.enqueue("Three")
>>> q.front()
'One'
>>> q.dequeue()
'One'
>>> q.dequeue()
'Two'
>>> q.front()
'Three'
>>> q.is_empty()
False
>>> q.enqueue("Four")
>>> q.dequeue()
'Three'
>>> q.dequeue()
'Four'
>>> q.is_empty()
True
```

Breid de wachtrij vervolgens uit met een methode `invert` die de wachtrij omkeert. Er wordt geen nieuwe wachtrij
gegenereerd. Je mag geen `data` velden wijzigen en geen nieuwe knopen alloceren. Je mag enkel de referenties 
van de gelinkte lijst manipuleren. Een mogelijk gebruik van de methode `invert` is als volgt:
```
>>> q = QueueList()
>>> for x in range(1,5):
...     q.enqueue(x)
...
>>> q.front()
1
>>> q.invert()
>>> q.front()
4
>>> q.dequeue()
4
>>> q.front()
3
>>> q.invert()
>>> q.front()
1
>>> q.dequeue()
1
>>> q.dequeue()
2
>>> q.front()
3
>>> q.invert()
>>> q.front()
3
>>> q.dequeue()
3
>>> q.invert()
>>> q.is_empty()
True
>>> q.enqueue(10)
>>> q.front()
10
```


