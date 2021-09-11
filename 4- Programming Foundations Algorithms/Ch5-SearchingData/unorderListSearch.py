items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def findItem(item, itemsList):
    for i in range(0, len(itemsList)):
        if item == itemsList[i]:
            return i
    return None


print(findItem(41, items))
print(findItem(100, items))
