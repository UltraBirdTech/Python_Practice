def bsort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

def quick(a):
    if len(a) in (0, 1):
        return a
