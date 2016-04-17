# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def getFactorsOf(num):
	toReturn = []
	for i in range(1, num+1):
		if num % i == 0:
			toReturn.append(i)
			
	return toReturn
	
def removeDuplicateFactors(list):
	for item in list:
		factorsOfItem = getFactorsOf(item)[:-1]
		for factor in factorsOfItem:
			if factor in list:
				list.remove(factor)
				print("removed", factor, "because this list has", item)
	

	
def isFactorOfEverything(num, list):
	for potFactor in list:
		if not num % potFactor == 0:
			return False
	return True


minNum = 1
maxNum = 20


mustBeDivisbleBy = list(range(minNum, maxNum+1))

removeDuplicateFactors(mustBeDivisbleBy)
print("Modified List:", mustBeDivisbleBy)


i = 0

while True:
	i += maxNum
	if(isFactorOfEverything(i, mustBeDivisbleBy)):
		print(i)
		break
	

	



