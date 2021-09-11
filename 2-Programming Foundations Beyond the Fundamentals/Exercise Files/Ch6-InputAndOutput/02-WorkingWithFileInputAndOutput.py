infile = open("values.txt", "rt")
outfile = open("values-totaled.txt", "wt")

print("Processing input")  # print in console

sum = 0
for l in infile:
    sum += int(l)
    print(l.rstrip(), file=outfile)  # print in outfile
print("\nTotal: "+str(sum), file=outfile)  # print in outfile
outfile.close()

print("complated")  # print in console
