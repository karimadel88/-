items = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(item, itemsList):
    listSize = len(itemsList)-1
    lowerIndex = 0
    upperIndex = listSize

    while(lowerIndex <= upperIndex):
        mid = (lowerIndex+upperIndex)//2
        if itemsList[mid] == item:
            return mid

        if item > itemsList[mid]:
            lowerIndex = mid+1
        else:
            upperIndex = mid - 1

    if lowerIndex > upperIndex:
        return None


print(binary_search(5, items))
print(binary_search(100, items))
