# Find the sum of all the multiples of 3 or 5 below 1000.

multiplesBelow = [] #list of multiples of 3 or 5 below 1000
for i in range (1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		multiplesBelow.append(i)
		
print(sum(multiplesBelow))
#233168
