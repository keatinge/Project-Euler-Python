power = 4
i = 2
total = 0
while i < 1000000:
    if sum([int(letter)**power for letter in str(i)]) == i:
        total += i
    i += 1
print(total)

