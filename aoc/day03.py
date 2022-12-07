from collections import Counter
import string
with open("day03.txt", "r") as f:
    bag = [i for i in f.read().strip().split('\n')]
part1 = []
part2 = []
common = []
for i in bag:
    part1 = i[:len(i)//2]
    part2 = i[len(i)//2:]
    print(i, part1, part2)
    for i in part1:
        if i in part2:
            common.append(i)


x = Counter(common)
print("Common: ", common)
print("X: ",x)

lowerAlpa = [str(i) for i in string.ascii_lowercase]
upperAlpha = [str(i) for i in string.ascii_uppercase]
alphas = lowerAlpa+upperAlpha
print("Alphas", alphas)

priors = {}
for count, value in enumerate(alphas, 1):
    priors[value] = count

newPrior={}
for k, v in priors.items():
    for a, b in x.items():
        if k == a:
            newPrior[k] = v

total = 0
for k,v in newPrior.items():
    if k in x:
        total = total + v
print("priors", priors)
print("newPrior: ", newPrior)
print(total)






