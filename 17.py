import math

def number_to_string_rep(num):
	#takes input of 573 and returns five hundred and seventythree 
	#spaces don't matter because you don't count them anyway
	below11 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
	below20 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	below100 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	
	wordString = ""
	
	if num == 1000:
		return "one thousand"
	elif num >= 100: #one hundred
		firstDigit = math.floor(num / 100)
		wordString = below11[firstDigit] + " hundred"
		toSubtract = (firstDigit * 100)
		num = num - toSubtract
		
		if not num == 0:
			wordString += " and "
	if num > 19: #twenty, thirty, fourty
		teens = True
		firstDigit = math.floor(num/10)
		wordString +=  below100[firstDigit-2]
		num = num - firstDigit * 10
	if num > 10:
		wordString +=  below20[num-11]
		num = num - num
	else:
		if not num == 0:
			wordString += below11[num]

		
	return wordString
		

fullString = ""	
for i in range(1, 1000+1):
	letterRep = number_to_string_rep(i)
	fullString += letterRep
	print(i, letterRep)
	
fullString = fullString.replace(" ", "")

print(len(fullString))