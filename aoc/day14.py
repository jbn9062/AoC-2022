from operator import itemgetter


with open("day14.txt", "rt") as f:
    input = f.read().strip().split("\n")

data = [i.split("->") for i in input]

coords = [[(int(j.split(",")[0].strip()), int(j.split(",")[1].strip())) for j in i] for i in data]

blocks = list()

for i in range(len(coords)):
    for j in range(len(coords[i])):
        coords = sorted(coords, key=itemgetter(0, 1))

#print(f"coords: {coords}")

filled = set()

for cordlst in coords:
    for i in range(len(cordlst) - 1):
        x1, y1 = cordlst[i]

        x2, y2 = cordlst[i + 1]

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                filled.add((x, y))

#print("\nFilled: ", filled)
max_x = max(x for x, y in filled)
max_y = max(y for x, y in filled)

# print(max_x)
# print(max_y)


floor = [(x, y) for x, y in filled if y == max_y]
print("floor",floor)

sand = (500, 0)


def sand_fall(floor, max_x, max_y, filled):
    src = (500, 0)
    x, y = 500, 0
    count = 0

    while y <= floor[1][1]:
        if (x, y+1) not in filled:
            y += 1
            continue

        if (x, y+1) in filled:
            if (x-1, y+1) not in filled:
                x -= 1
                y += 1
                continue

            elif (x-1, y+1) in filled and (x+1, y+1) not in filled:
                x += 1
                y += 1
                continue

        if (x, y+1) in filled and (x-1, y+1) in filled and (x-1, y+1) in filled:
            filled.add((x, y))
            count += 1
            x, y = 500, 0

        if y == floor[1][1] and ((x-1, y+1) not in filled or (x+1, y+1) not in filled):
            return count

        if y+1 > floor[1][1]:
            break
    return count


print(sand_fall(floor, max_x, max_y, filled))
