with open("day08.txt") as file:
    data = [row.strip() for row in file.readlines()]

ROWS = len(data)  # num of rows
COLUMNS = len(data[0])  # num of columns

edges = (ROWS * 2) + ((COLUMNS - 2) * 2)  # all trees on edges are visible
total = edges  # add edges to total visible trees
scores = []  # track the scenic scores

# Iterate through trees not on edges
for row in range(1, ROWS - 1):
    for col in range(1, COLUMNS - 1):
        tree = data[row][col]  # Tree that we are looking at

        # Get all horizontal & vertical trees
        left1 = [data[row][col - i] for i in range(1, col + 1)]
        right1 = [data[row][col + i] for i in range(1, COLUMNS - col)]
        up1 = [data[row - i][col] for i in range(1, row + 1)]
        down1 = [data[row + i][col] for i in range(1, ROWS - row)]
        '''print("left ", left1)
        print("right ", right1)
        print("up: ", up1)
        print("Down: ", down1)'''
        # === PART 1 ===
        # Check if tallest tree on all sides blocks our view of the tree
        if max(left1) < tree or max(right1) < tree or max(up1) < tree or max(down1) < tree:
            total += 1

        # === PART 2 ===

        # Finding scenic score
        score = 1
        for lst in (left1, right1, up1, down1):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:
                    tracker += 1
                    break

            score *= tracker

        scores.append(score)

print("Answer to part 1:", total)
print("Answer to part 2:", max(scores))