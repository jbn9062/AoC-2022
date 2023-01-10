import time
from collections import deque
import string


with open("day12.txt", "rt") as f:
    grid = [line.strip() for line in f.readlines()]
alphabets = dict(zip(string.ascii_lowercase, range(1, 27)))
alphabets['S'] = 0
alphabets['E'] = 28
count = 0

def findPos(grid, alpha):
    pos = ()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == alpha:
                 pos = (row, col)
    return pos

start = findPos(grid, "S")
goal = findPos(grid, "E")
def elevation(ch):
    height = 0
    for i in alphabets.keys():
        if i == ch:
            height = alphabets[ch]
        if ch == 'S':
            height = alphabets['a']
        if ch == 'E':
            height = alphabets['z']
    return height

right = (1,0); left = (-1,0); up = (0,-1); down = (0,1)
neighbors = []
directions = [right, left, up, down]

def find_neighbors(grid, pos, goal):
    right = (1, 0)
    left = (-1, 0)
    up = (0, -1)
    down = (0, 1)
    neighbors = []
    directions = [right, left, up, down]

    x, y = pos[0], pos[1]


    if  y + left[0] >= 0 and y + left[0] < len(grid[0]):
        if (elevation(grid[x][y + left[0]]) - elevation(grid[x][y])) <= 1:
            neighbors.append((x, y + left[0]))  # Neighbor Left

    if  x + up[1] >= 0 and x + up[1] < len(grid):
        if (elevation(grid[x + up[1]][y]) - elevation(grid[x][y])) <= 1:
            neighbors.append((x + up[1], y ))  # Neighbor Up

    if y + right[0] >= 0 and y + right[0] < len(grid[0]):
        if (elevation(grid[x][y + right[0]]) - elevation(grid[x][y])) <= 1:
            neighbors.append((x , y + right[0]))  # Neighbor Right

    if x + down[1] >= 0 and x + down[1] < len(grid):
        if (elevation(grid[x + down[1]][y ]) - elevation(grid[x][y])) <= 1:
            neighbors.append((x + down[1], y ))  # Neighbor Down

    return neighbors


def path(start, goal):

    visited = set()
    que = deque([start])
    distances = {start:0}
    while que:
        curr_node = que.popleft()
        if curr_node == goal:
            return distances[goal]
        for neibr in find_neighbors(grid, curr_node, goal):
            if neibr not in visited:
                que.append((neibr))
                visited.add(neibr)
                if neibr not in distances:
                    distances[neibr] = distances[curr_node] + 1
    return -1
print(path(start, goal))

def part_2(grid, goal):

    starts = [(row_i, col_i) for row_i, row in enumerate(grid) for col_i, col in enumerate(row) if col == 'a']
    paths = []
    for i in starts:
            start = i
            if path(start, goal) != -1:
                paths.append(path(start, goal))
    return min(paths)

start_time = time.time()
print(part_2(grid, goal))
end_time = time.time()

print(f" {end_time - start_time} seconds elapsed") # 28 seconds