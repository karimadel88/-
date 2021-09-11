def powe(num, power):
    if power == 0:
        return 1
    else:
        return num * powe(num, power-1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


print(powe(2, 2))
print(factorial(0))
print(factorial(3))
