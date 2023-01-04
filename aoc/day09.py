import math

with open("day09.txt", "rt") as f:
    data = [i.split() for i in f.readlines()]

direction = [i[0] for i in data]
moves = [int(i[1]) for i in data]
data = list(zip(direction, moves))
print(data)

# knots = [[0,0], [0,0]] #  knots[0] > tail    knots[1] > head
head = [0, 0]
tail = [0, 0]
side = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def isTouching(head, tail):
    absX = abs(head[0] - tail[0])
    absY = abs(head[1] - tail[1])
    distance = math.sqrt((absX ** 2) + (absY ** 2))
    if distance <= 1:
        return True
    else:
        return False


def tail_moves(head, tail):
    if not isTouching(head, tail):
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]
        absX = abs(dx)
        absY = abs(dy)
        tail[0] += (0 if dx == 0 else dx // absX)
        tail[1] += (0 if dy == 0 else dy // absY)
    return tail.copy()


tail_mvs = [[0,0]]
head_mvs = []

for i in data:
    direction = i[0]
    step = i[1]
    for i in range(step):
        if direction == 'R':
            head[0] += 1
        elif direction == 'L':
            head[0] -= 1
        elif direction == 'U':
            head[1] += 1
        elif direction == 'D':
            head[1] -= 1
        head_mvs.append(head.copy())
        if not isTouching(head, tail):
            for i in range(step - 1):
                tail_mvs.append(tail_moves(head, tail))

tail_positions = set(tuple(i) for i in tail_mvs)
print(len(tail_positions))


