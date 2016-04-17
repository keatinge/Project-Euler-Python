#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(input):
	strInput = str(input)
	
	if strInput == strInput[::-1]:
		return True
	return False
	



smallest = 100
biggest = 999


palindomes = []

for i in range(biggest, smallest-1, -1):
	for j in range(biggest, smallest-1, -1):
		product = i * j
		if isPalindrome(product):
			palindomes.append(product)
			

sortedList = sorted(palindomes)
print(sortedList[-1:][0])
