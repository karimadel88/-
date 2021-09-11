
items = dict({
    "k1": 1,
    "k2": 2,
    "k3": 3
})

print(items)

items2 = {}
items2["k1"] = 5
items2["k2"] = 6
items2["k3"] = 7

for key, val in items2.items():
    print("Key : ", key, " value : ", val)
