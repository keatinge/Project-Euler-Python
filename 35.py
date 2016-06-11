import itertools
import math

def isPrime(num):
    if num == 1: return False
    if num == 2: return True

    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True




def isCircPrime(num):
    strNum = list(str(num))
    for i in range(len(strNum)):
        strNum.append(strNum.pop(0))
        thisNum = int("".join(strNum))
        if not isPrime(thisNum):
            return False

    return True
        


maxNum = 1000000
tally = 0
for i in range(1, maxNum):
    if isCircPrime(i):
        tally += 1
        print(tally, ":", i)

print("There are", tally, "circular primes below", maxNum)
