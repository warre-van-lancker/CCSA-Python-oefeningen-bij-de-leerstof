class AchtPuzzel:

    BUREN = {0 : {("R", 1),("O", 3)},   1 : {("L", 0),("R", 2),("O", 4)},   2 : {("L",1),("O",5)},
             3 : {("B",0),("R",4),("O",6)}, 4 : {("B",1),("L", 3),("R", 5),("O",7)}, 5 : {("B",2),("L", 4),("O",8)},
             6 : {("B",3),("R",7)},   7 : {("B",4),("L",6),("R",8)},   8 : {("B",5),("L",7)} 
            }

    def __init__(self, bord="123456780"):
        pass


    def __str__(self):
        return self.bord[:3] +  "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"


    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False


    def __hash__(self):
        return hash(self.bord)

    
    def opvolgers(self):
        pass
    
    def aantal_verkeerd(self, other):
        pass

    def manhattan_heuristiek(self, other):
        pass


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        pass

    ## Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        pass

    def geef_actie_sequentie(self):
        pass
    
def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost= lambda s,a : 1):
    pass
