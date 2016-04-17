import math
import time


def isPrime(num):
	
	for i in range(2,num):
		if (num % i == 0):
			return False
	return True

	
def getFactorsFast(num):
	factorList = []
	maxSearch = math.ceil(math.sqrt(num))
	
	for i in range(1, maxSearch+1):
		if num % i == 0:
			bigFactor = int(num/i)
			factorList.append(bigFactor)
			factorList.append(i)
	return factorList

startTime = time.time()
number = 600851475143
factorList = reversed(sorted(getFactorsFast(number)))


for number in factorList:
	if isPrime(number):
		print(number)
		print("Total Time: " + str(time.time() - startTime)[:5] + " seconds")
		exit()
