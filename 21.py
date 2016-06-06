import math
def sumOfDivisors(num):
	sum = 1
	
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			sum += i
			sum += num / i
			

	return int(sum)
	

total = 0
for i in range (1, 10001):
	sumDivs = sumOfDivisors(i)
	if sumOfDivisors(sumDivs) == i:
		if sumDivs != i:
			print(i)
			total += i

print("Answer:", total)
	
