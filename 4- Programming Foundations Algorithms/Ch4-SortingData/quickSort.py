items = [15, 3, 5, 4]


def quickSort(dateset, first, last):
    if(first < last):
        pivotIndex = partition(dateset, first, last)

        quickSort(dateset, first, pivotIndex-1)
        quickSort(dateset, pivotIndex-1, last)


def partition(dateValues, first, last):
    pivoteValue = dateValues[first]
    lower = first + 1
    upper = last

    done = False

    while not done:
        while lower <= upper and dateValues[lower] <= pivoteValue:
            lower += 1
        while dateValues[upper] >= pivoteValue and upper >= lower:
            upper -= 1

        if upper < lower:
            done = True
        else:
            temp = dateValues[lower]
            dateValues[lower] = dateValues[upper]
            dateValues[upper] = temp

    temp = dateValues[first]
    dateValues[first] = dateValues[upper]
    dateValues[upper] = temp

    return upper


quickSort(items, 0, len(items)-1)
print(items)
