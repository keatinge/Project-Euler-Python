import itertools

nums = list(range(0,10))
perms = list(itertools.permutations(nums))
combinedPerms = ["".join([str(x) for x in tup]) for tup in perms]
sortedPerms = sorted(combinedPerms)
print(combinedPerms[999999])
#2783915460
