items = ["apple", "pear", "orange", "banana",
         "apple", "orange", "apple", "pear", "banana"]
filter = dict()
for key in items:
    filter[key] = 0

result = set(filter.keys())

print(result)
