items = [1, 2, 9, 36, 10, 3, 45]


def findMax(items):
    if len(items) == 1:
        return items[0]

    val1 = items[0]
    val2 = findMax(items[1:])

    if val1 > val2:
        return val1
    else:
        return val2


print(findMax(items))
