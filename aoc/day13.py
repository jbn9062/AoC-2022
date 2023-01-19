from functools import cmp_to_key
with open("day13.txt","rt") as f:
    file = f.read().strip().split("\n\n")

data = [i.strip().split("\n") for i in file]

packets = [[eval(j) for j in i] for i in data]

def comp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        elif l == r:
            return 0
        else:
            return -1

    elif isinstance(l, list) and isinstance(r, list):
        for k,j in zip(l, r):
            x = comp(k, j)
            if x != 0:
                return x

        if len(l) < len(r):
            return 1
        elif len(l) > len(r):
            return -1
        else:
            return 0

    elif isinstance(l, int) and isinstance(r, list):
        return comp([l], r)
    elif isinstance(l, list) and isinstance(r, int):
        return comp(l, [r])

    return 0

count = 0
for index, i in enumerate(packets, start=1):
    l, r = i
    x = comp(l, r)
    if x != -1 and x!= 0:
        count += index

print("part1: ",count)

#  Part 2



def part2(packets):
    ordered = [[[2]], [[6]]]
    decoder = 1
    for index, i in enumerate(packets, start=1):
        l, r = i
        ordered.append(l)
        ordered.append(r)
    ordered = sorted(ordered, key=cmp_to_key(comp), reverse=True)
    for index, i in enumerate(ordered, start=1):
        if i == [[2]]:
            decoder *= index
        if i == [[6]]:
            decoder *= index
    return decoder
print("Part2: ",part2(packets))



### Reference:
# https://github.com/calebjcourtney/advent-of-code/blob/main/2022/python/day13.py
# https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_13/day_13_p1.py