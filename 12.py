import math
import time

def get_factors(num):
	factors = 0
	for i in range(1,math.ceil(math.sqrt(num))):
		if num % i == 0:
			#i only check below the square root, but every factor below the sqrt
			#also has a corresponding factor above the sqrt
			factors += 2
	return factors
	
num = 1
iter = 2

while 1:
	factors = get_factors(num)
	if factors > 500:
		print(num)
		break
	#loop the triangle number sequence indefinitely 
	num = num + iter
	iter += 1
	