# function to get gcd
# steps
# if a havnt remind b is greatest
# else a is b and b is reminder


def gcd(a, b):
    while(b != 0):
        t = a
        a = b
        b = t % b
    return a

# 20 8 ==>
# t = 20 a=8 # b=4
# t =8 a=4 b=0 # a as return


print(gcd(60, 96))
print(gcd(20, 8))
