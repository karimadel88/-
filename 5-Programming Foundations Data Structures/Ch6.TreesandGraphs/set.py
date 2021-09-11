primarColors = set(["red", "blue", "yellow"])
# to dont allow insert we can use frozenset

color = "green"
if color.lower() in primarColors:
    print(color + " Is a primary color")
else:
    print(color + " Is not a primary color")


letters = set([5, 6])
letters.add(1)

print(letters)
