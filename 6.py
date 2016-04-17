import math

def sumOfSquaresOfFirstNNumbers(num):
	listOfSquares = []
	for i in range(1, num+1):
		square = math.pow(i,2)
		listOfSquares.append(square)
	
	return sum(listOfSquares)
	
def squareOfSumOfFirstNNumbers(num):
	numList = range(1, num+1)
	sumOfNumList = sum(numList)
	squaredNumListSum = math.pow(sumOfNumList, 2)
	return squaredNumListSum
		
	
	
toCalc = 100
sumSquare = sumOfSquaresOfFirstNNumbers(toCalc)
squareSum = squareOfSumOfFirstNNumbers(toCalc)



answer = squareSum - sumSquare
print(answer)
