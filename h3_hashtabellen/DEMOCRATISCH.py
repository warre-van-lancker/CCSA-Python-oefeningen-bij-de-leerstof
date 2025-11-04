class Hashtabel:
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende  

    def __init__(self, lengte=10):
        self.n = lengte
        self.table = lengte * [None]

    def bereken_index(self, char):
        return ((ord(char.upper()) - ord('A') + 1) * 11) % self.n

    def voegToe(self, data):
        for char in data:
            index = self.bereken_index(char)
            if self.table[index] is None:
                self.table[index] = self.Knoop(char)
            else:
                self.table[index] = self.Knoop(char, self.table[index])

    def toString(self):
        out = []
        for item in self.table:
            if item is not None:
                cur = item
                chain = []
                while cur is not None:
                    chain.append(cur.data)
                    cur = cur.volgende
                out.append(chain)
            else:
                out.append(None)
        return out        

if __name__ == "__main__":
    tabel = Hashtabel(5)
    tabel.voegToe("DEMOCRATISCH")
    print(tabel.toString())