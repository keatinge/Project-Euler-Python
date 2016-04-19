import math

ans = math.pow(2,1000)
ansString = str(int(ans))

print(ansString)

total = 0
for letter in ansString:
	total += int(letter)
	
print(total)