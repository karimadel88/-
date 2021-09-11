def bubbleSort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        print("Current State : ", dataset)


def main():

    list1 = [23, 8, 15, 17, 4, 40, 11, 31]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
