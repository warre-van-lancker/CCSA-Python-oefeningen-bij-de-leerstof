def two_sum(getallen, doel):
    for i, getal1 in enumerate(getallen):
        for j, getal2 in enumerate(getallen):
            if i != j and getal1 + getal2 == doel:
                return i, j
    return None

def two_sum_beter(getallen, doel):
    for i in range(len(getallen)):
        for j in range(i + 1, len(getallen)):
            if getallen[i] + getallen[j] == doel:
                return i, j
    return None


def two_sum_hash(getallen, doel):
    tabel = (doel + 1) * [None]
    for index, getal in enumerate(getallen):
        if getal <= doel:
            if tabel[doel - getal] is not None:
                return tabel[doel - getal], index
            tabel[getal] = index
    return None
