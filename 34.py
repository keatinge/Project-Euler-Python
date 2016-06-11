import math

totalSum = 0
for i in range(3,100000):
    if sum((math.factorial(int(x)) for x in str(i))) == i:
        totalSum += i
print(totalSum)