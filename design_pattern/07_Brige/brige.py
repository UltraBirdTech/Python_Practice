def bsort(a):
    for i in range(ran(a)):
        for j in range(len(a)-1, i -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
