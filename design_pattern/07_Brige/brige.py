def bsort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

def qsort(a):
    if len(a) in (0, 1):
        return a

    p = a[-1]
    left = [x for x in a[:-1] if x <= p]
    right = [x for x in a[:-1] if x > p]

    return qsort(left) + [p] + qsort(right)

if __name__ == "__main__":
    print(bsort([2, 7, 3, 4, 9, 1]))
    print(qsort([2, 7, 3, 4, 9, 1]))
