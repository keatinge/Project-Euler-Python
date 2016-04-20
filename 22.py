def get_name_val(name):
	letterVal = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
	sum = 0
	for letter in name:
		sum+= letterVal[letter]
	return sum

file = open("p022_names.txt")
names = file.read().replace('"', '').split(",")
file.close()



names = sorted(names)

sums = 0
for i, name in enumerate(names):
	position = i+1
	value = get_name_val(name)
	
	totalScore = value * position
	sums += totalScore
print(sums)
	