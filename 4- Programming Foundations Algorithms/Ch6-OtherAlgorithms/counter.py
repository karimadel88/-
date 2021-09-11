items = ["apple", "pear", "orange", "banana",
         "apple", "orange", "apple", "pear", "banana"]

counter = dict()

for key in items:
    if(key in counter.keys()):
        counter[key] += 1
    else:
        counter[key] = 1

print(counter)
