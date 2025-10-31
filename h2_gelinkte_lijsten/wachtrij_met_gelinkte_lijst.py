from doctest import testmod

class QueueList:
    """
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
    """

    class Knoop:

        def __init__(self,data=None,volgende=None) -> None:
            self.data = data
            self.volgende = volgende

    def __init__(self) -> None:
        self.kop = None
        self.staart = None

    def is_empty(self):
        return self.kop is None

    def enqueue(self,data):
        hulp = self.Knoop(data)
        if self.is_empty():
            self.kop = hulp
        else:
            self.staart.volgende = hulp
        self.staart = hulp

    def front(self):
        return self.kop.data

    def dequeue(self):
        out = self.kop
        self.kop = self.kop.volgende
        if self.is_empty():
            self.staart = None
        return out.data
    
    def invert(self):
        vorige = None
        huidige = self.kop
        while huidige is not None:
            volgende = huidige.volgende
            huidige.volgende = vorige
            vorige = huidige
            huidige = volgende
        self.kop, self.staart = self.staart, self.kop
            
        

if __name__ == "__main__":
    testmod()