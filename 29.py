maxNum = 100
terms = set()
for a in range(2,maxNum+1):
    for b in range(2,maxNum+1):
        terms.add(a**b)

print(len(terms))