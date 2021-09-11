# String is an array of characters
# Connevtion single sting and anothet to get new string or line of chars.
# programming + " " + language = programming language

value = input("Enter ypur number : ")
print(value)
# print(type(value)) defual of input functiuon (String value)

# can print that without any bugs as str + str
print(value + " " + " is my fav. number")

print(value * 10)  # can repeat no multiply by 10 ==> 505050505050..

# to slove thit bug can cast value from string to integer number
value_int = int(value)

print(value_int * 10)  # value * 10 == value0
