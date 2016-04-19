import math

#original solution
digits = []
[digits.append(int(digit)) for digit in str(math.factorial(100))]
print(sum(digits))

#pythonic solution
digits = list(str(math.factorial(100)))
digits = map(int,digits)
print(sum(digits))

#easy to read solution
digits = str(math.factorial(100))
sum = 0
for digit in digits:
	sum += int(digit)
print(sum)