# from typing import Tuple
# print("heloo ")

# k = 2


# def xa():
#     global k
#     k = 3
#     print(k)
#     print("that gloabl")


# xa()
# print(k)

# # in , len() , not in ,str[start : end] to slice ==> string

# a = "karim"
# k = a.upper()
# print(k)

# age = str(36)
# txt = "My name is John, I am " + age
# print(txt)

# print(bool("Hello"))

# print(int(8/3))

# print(8//3)

# # lists
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0]+numbers[len(numbers)-1])  # 1 + 5 = 6

# # dictionery

# files = {
#     "forms": 1,
#     "an": 2
# }

# print(files["forms"])

# age = 13

# print(15 >= age + 2)

# list1 = [1, False, "karim"]
# #list1 = list((1, 2, 3))

# tu = (1, 2, 3)
# #tu[1] = 5
# # print(tu[1])

# # print(list1[1])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # thislist[1:3] = ["blackcurrant", "watermelon"]
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist[1:2] = ["blackcurrant", "watermelon"]
# # print(thislist)


# # x = int(input())
# # y = int(input())

# # if (x % 2) == 0:
# #     y += 1

# # print(y)
# # x, y = 5, 6
# # print(x)
# # print(y)
# # print("---------")

# # a = [5, 9, 7, 8]
# # # print(a)
# # a.sort()
# # print(a)
# # b = a.copy()
# # print(b)
# # a.insert(1, 5)
# # a.pop()
# # print(a)
# # n = len(a)
# # i = 0
# # while i < n:
# #     print(a[i])
# #     b = 0
# #     if b == 0:
# #         break
# #     i += 1

# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")

# appends ==> to add from last
a = [5, 6, 7, 8, 9]
a.append(10)
a.insert(0, 1)

# extend ==> to add old array to new array
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a1.extend(a2)   # a1+=a1+a2
# remove
a1.remove(1)  # ==> Value
a1.pop(1)    # ==> Index if we didnt specify the index it remove last element
# del a1[5]    # ==> keyword del can delete item by specify index of it
# print(a1)
a2.clear()
print(a2)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
