def bubbleSort(a):
    temp = 0

    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp

    return a