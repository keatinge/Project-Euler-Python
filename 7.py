import math
#What is the 10,001st prime number?

def isPrime(num):
	#loop from 2 up to and including sqrt(num)
	for i in range(2, int(math.sqrt(num))+1): 
		if num % i == 0:
			return False
	return True

maxNumber = 10001
primesList = []

i = 0
while len(primesList) <= maxNumber:
	i += 1
	if isPrime(i):
		primesList.append(i)
	
#print last item in the list
print(primesList[-1:][0])