import math

def isPrime(num):
	if (num == 2):
		return True
	
	for i in range(2, math.ceil(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True





	
maxNum = 2000000
primeList = []

for i in range(2, maxNum):
	if isPrime(i):
		primeList.append(i)
	
print(len(primeList))
print(sum(primeList))
