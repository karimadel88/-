
item = [1, 2, 3, 4, 5]
item2 = [2, 1, 3, 4]


def isSorted(items):
    for i in range(0, len(items)-1):
        if(items[i] > items[i+1]):
            return False
    return True


print(isSorted(item))
print(isSorted(item2))
