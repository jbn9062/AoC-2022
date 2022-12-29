with open("day08.txt", "rt") as f:
    heights = [list(map(int, l.strip())) for l in f]

def part1(heights):
    count = 0
    for i in range(1, len(heights) - 1):
        for j in range(1, len(heights[i]) - 1):
            # check if tree is visible from right
            if heights[i][j] > max(heights[i][j + 1:]):
                count += 1
            # check if tree is visible from left
            elif heights[i][j] > max(heights[i][:j]):
                count += 1
            # check if tree is visible from above
            elif heights[i][j] > max([line[j] for line in heights[:i]]):
                count += 1
            # check if tree is visible from below
            elif heights[i][j] > max([line[j] for line in heights[i + 1:]]):
                count += 1
    # Adding the number of trees at all four sides
    count += len(heights) * 2  # Adding the number of trees at either side of each rows
    count += len(heights[0]) - 2  # Adding trees that are at the top of the grid
    count += len(heights[0]) - 2  # Adding trees that are at the bottom of the grid

    return (count)

def part2(heights):
    scenic_scores = []
    for line in range(1, len(heights)):
        for col in range(1, len(heights[line])):
            tree = heights[line][col]
            left = [heights[line][col-k-1] for k in range(1, col+1)]
            right = [heights[line][col+k] for k in range(1, len(heights[line])-col)]
            up = [heights[line-k][col] for k in range(1, line+1)]
            down = [heights[line+k][col] for k in range(1, len(heights[line])-line)]
            scenic = 1
            for i in (left, right, up, down):
                count = 0
                for j in range(len(i)):
                    if tree > i[j]:
                        count += 1
                    elif tree == i[j]:
                        count += 1
                        break
                scenic *= count
            scenic_scores.append(scenic)
    return (max(scenic_scores))

print("Part1: ", part1(heights))
print("PArt2: ", part2(heights))