with open("day18.txt", "rt") as f:
    data = f.read().split("\n")

coords = [i.split(",") for i in data]
coords = [tuple(int(j) if j.isdigit() else j for j in i)for i in coords]

print("coords:", coords)


def part1(coords):
    area = 0
    adj = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    for i in range(len(coords)):
        x, y, z = coords[i]
        for j in range(len(adj)):
            dx, dy, dz = adj[j]
            if (x+dx, y+dy, z+dz) not in coords:
                area += 1
    return area

print("Part1: ", part1(coords))



## Reference
# https://www.youtube.com/watch?v=LC62vsvPjZc




