with open("day09.txt", "rt") as f:
    data = [i.split() for i in f.readlines()]

direction = [i[0] for i in data]
moves = [int(i[1]) for i in data]
data = list(zip(direction, moves))

knots_p1 = [[0, 0], [0, 0]]
knots_p2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


side = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

tail_mvs = [[0, 0]]

def isTouching(head, tail):
    absX = abs(head[0] - tail[0])
    absY = abs(head[1] - tail[1])
    distance = ((absX ** 2) + (absY ** 2))
    if distance <= (2):
        return True
    else:
        return False


def tail_moves(knots):
    for i in range(len(knots)-2, -1, -1):
        if not isTouching(knots[i+1], knots[i]):
            dx = knots[i+1][0] - knots[i][0]
            dy = knots[i+1][1] - knots[i][1]
            absX = abs(dx)
            absY = abs(dy)
            knots[i][0] += (0 if dx == 0 else dx // absX)
            knots[i][1] += (0 if dy == 0 else dy // absY)
    return knots



def make_moves(knots):
    for i in data:
        direction = i[0]
        step = int(i[1])
        move_to = side[direction]
        for k in range(step):
            knots[-1][0] += move_to[0]
            knots[-1][1] += move_to[1]
            knots = tail_moves(knots)
            tail_mvs.append(knots[0].copy())

    tail_positions = set(tuple(i) for i in tail_mvs)
    return len(tail_positions)



print("Part 1: ", make_moves(knots_p1))
print("Part 1: ", make_moves(knots_p2))