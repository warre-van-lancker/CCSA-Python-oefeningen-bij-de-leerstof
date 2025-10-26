def bubble_sort(a):
    n = len(a)
    uitgevoerd = 0
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            uitgevoerd += 1
            if (a[j - 1] > a[j]):
                a[j - 1], a[j] = a[j], a[j - 1]
        print(a)
    print(f"Voor een rij van lengte {n} werd het if-statement {uitgevoerd} keer uitgevoerd")

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    bubble_sort(a)