from collections import deque # wachtrij in Python
from doctest import testmod

def precies_een_verschillend(woord1, woord2) -> bool:
    """
    >>> precies_een_verschillend("span", "spat")
    True
    >>> precies_een_verschillend("test", "tast")
    True
    >>> precies_een_verschillend("test", "testje")
    False
    >>> precies_een_verschillend("test", "test")
    False
    >>> precies_een_verschillend("testje", "test")
    False
    >>> precies_een_verschillend("TEST", "test")
    False
    """
    if len(woord1) != len(woord2):
        return False
    teller = 0
    for i in range(len(woord1)):
        if woord1[i] != woord2[i]:
            teller += 1
    return teller == 1    
    
def maak_graaf(woorden) -> dict:
    woordenboek = {}
    for key in woorden:
        woordenboek[key] = set()
        for value in woorden:
            if precies_een_verschillend(key, value):
                woordenboek[key].add(value)
    return woordenboek

def kortste_pad(graaf,woord) -> dict:
    """
    >>> words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
    >>> graaf = maak_graaf(words)
    >>> kortste_pad(graaf, "aa")
    {'aa': 'aa', 'ab': 'aa', 'ac': 'aa', 'ad': 'aa', 'ba': 'aa', 'bb': 'ab', 'bc': 'ac', 'bd': 'ad', 'ca': 'aa', 'cb': 'ab', 'cc': 'ac', 'cd': 'ad', 'da': 'aa', 'db': 'ab', 'dc': 'ac', 'dd': 'ad'}
    """
    P = {woord:None for woord in graaf.keys()}
    P[woord] = woord
    Q = deque([woord])
    while len(Q) > 0:
        v = Q.popleft()
        for w in sorted(graaf[v]):
            if P[w] is None:
                P[w] = v
                Q.append(w)
    return P

def geef_pad(voorgangers,woord) -> list:
    """
    >>> words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
    >>> graaf = maak_graaf(words)
    >>> pred = kortste_pad(graaf, "aa")
    >>> geef_pad(pred, "dd")
    ['aa', 'ad', 'dd']
    >>> geef_pad(pred, "aa")
    ['aa']
    >>> geef_pad(pred, "ba")
    ['aa', 'ba']
    """
    if voorgangers[woord] is None:
        return None
    L = [woord]
    while voorgangers[woord] != woord:
        woord = voorgangers[woord]
        L.insert(0, woord)
    return L

if __name__ == "__main__":
    testmod()