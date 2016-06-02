a = i = 0
b = 1
while True:
    if len(str(a)) == 1000:
        print(i, a)
        break
    b, a = a+b, b
    i += 1
