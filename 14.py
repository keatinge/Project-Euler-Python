def get_output_chain_len(startingNum):
	n = startingNum
	
	length = 0
	while 1:
		length += 1
		if n == 1:
			break
		if n % 2 == 0:
			n = n / 2
		else:
			n = (3 * n) + 1
		
	return length
	
	
maxLen = 0
maxStartingNum = 0
for i in range(1, 1000000):
	print(i)
	currentLength = get_output_chain_len(i)
	
	if currentLength > maxLen:
		maxStartingNum = i
		maxLen = currentLength
		
print(maxStartingNum)
print(maxLen)



	

