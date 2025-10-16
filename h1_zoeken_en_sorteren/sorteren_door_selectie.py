def selection_sort_vooraan(a):
    n = len(a)
    for i in range(n-1):
        pos = i
        min = a[i]
        for j in range(i + 1, n):
            if a[j] < min:
                pos = j
                min = a[j]
        a[pos] = a[i]
        a[i] = min
        print(a)

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_vooraan(a)
