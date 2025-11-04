class HashSet:

    def __init__(self, max_size=10):
        self.n = max_size
        self.table = max_size * [None]

    def hashfunctie(self, item):
        return hash(item) % self.n
    
    def add(self, item):
        index = self.hashfunctie(item)
        iteraties = 1
        while iteraties <= self.n and not self.table[index] in [None, 'X']:
            print(index)
            index = (index + 1) % self.n
            iteraties += 1
        if iteraties > self.n:
            raise ValueError
        self.table[index] = item
        return index

    def index_of(self, item):
        index = self.hashfunctie(item)
        iteraties = 1
        while iteraties <= self.n and not self.table[index] in [None, item]:
            print(index)
            index = (index + 1) % self.n
            iteraties += 1
        if self.table[index] == item:
            return index
        return -1
    
    def delete(self, item):
        index = self.index_of(item)
        if index != -1:
            self.table[index] = 'X'
            return True
        return False

    





