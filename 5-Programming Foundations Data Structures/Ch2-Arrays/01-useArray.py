perStudentPetCount = [0, 1, 0, 2, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]
numOfStudent = len(perStudentPetCount)

sum = 0
for x in perStudentPetCount:
    sum += x

average = sum // numOfStudent

print(perStudentPetCount[3])
# print(perStudentPetCount[100]) # out of renge

print(average)
