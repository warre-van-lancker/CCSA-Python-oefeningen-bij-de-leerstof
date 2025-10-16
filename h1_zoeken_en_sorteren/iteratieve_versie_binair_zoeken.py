def zoek_binair(zoekItem, rij):
    l = 0; r = len(rij) - 1
    while l != r:
        m = (l + r) // 2
        print(f"{l}, {r}")
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    if rij[l] == zoekItem:
        return l
    else:
        return -1