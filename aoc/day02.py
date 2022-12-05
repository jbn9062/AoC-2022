
def getInput():
    with open("day02.txt", "r") as f:
        x = [list(i) for i in f.read().split('\n')]
    for i in x:
        i.remove(' ')
    return x

def findScore(x):
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for i, j in x:
        if i == 'A' and j == 'X':
            score = score + points.get('X') + 3
        elif i == 'A' and j == 'Y':
            score = score + points.get('Y') + 6
        elif i == 'A' and j == 'Z':
            score = score + points.get('Z')
        elif i == 'B' and j =='X':
            score = score + points.get('X')
        elif i == 'B' and j == 'Y':
            score = score + points.get('Y') + 3
        elif i == 'B' and j == 'Z':
            score = score + points.get('Z') + 6
        elif i == 'C' and j == 'X':
            score = score + points.get('X') + 6
        elif i == 'C' and j == 'Y':
            score = score + points.get('Y')
        elif i == 'C' and j == 'Z':
            score = score + points.get('Z') + 3

    print(points)
    return score

def task2(x):
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    score2 = 0
    for i in range(len(x)):

    for i, j in x:
        if i == 'A' and j == 'X':
            score = score2 + points.get('X') + 3
        elif i == 'A' and j == 'Y':
            score = score2 + points.get('Y') + 6
        elif i == 'A' and j == 'Z':
            score = score2 + points.get('Z')
        elif i == 'B' and j == 'X':
            score = score2 + points.get('X')
        elif i == 'B' and j == 'Y':
            score = score2 + points.get('Y') + 3
        elif i == 'B' and j == 'Z':
            score = score2 + points.get('Z') + 6
        elif i == 'C' and j == 'X':
            score = score2 + points.get('X') + 6
        elif i == 'C' and j == 'Y':
            score = score2 + points.get('Y')
        elif i == 'C' and j == 'Z':
            score = score2 + points.get('Z') + 3

x = getInput()
print(getInput())
print(findScore(x))
print(task2(x))

