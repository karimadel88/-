# comlixity O(nlogn)

items = [23, 8, 15]


def mergeSort(dateset):
    if len(dateset) > 1:
        mid = len(dateset)//2
        l = dateset[:mid]
        r = dateset[mid:]

        mergeSort(l)
        mergeSort(r)

        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                dateset[k] = l[i]
                i += 1
            else:
                dateset[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            dateset[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            dateset[k] = r[j]
            j += 1
            k += 1


mergeSort(items)
print(items)
