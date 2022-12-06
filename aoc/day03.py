from collections import Counter
import string
with open("day03.txt", "r") as f:
    bag = [list(i) for i in f.read().split('\n')]
    print(bag)
part1 =[]
part2 = []
common = []
for i in bag:
    part1 = i[:len(i)//2]
    part2 = i[len(i)//2:]
    for i in part1:
        if i in part2:
            common.append(i)

x = Counter(common)
print("Common: ", common)
print(x)


