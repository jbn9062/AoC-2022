
def getInput():
    with open("day02.txt", "r") as f:
        x = [list(i) for i in f.read().split('\n')]
    for i in x:
        i.remove(' ')
    return x

def task1(x):
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
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 3, 'Y': 0, 'Z': 3}
    score2 = 0

    for i, j in x:
        if i == 'A' and j == 'X':
            score2 = score2 + points.get('C') + 0
        elif i == 'A' and j == 'Y':
            score2 = score2 + points.get('A') + 3
        elif i == 'A' and j == 'Z':
            score2 = score2 + points.get('B') + 6
        elif i == 'B' and j == 'X':
            score2 = score2 + points.get('A') + 0
        elif i == 'B' and j == 'Y':
            score2 = score2 + points.get('B') + 3
        elif i == 'B' and j == 'Z':
            score2 = score2 + points.get('C') + 6
        elif i == 'C' and j == 'X':
            score2 = score2 + points.get('B') + 0
        elif i == 'C' and j == 'Y':
            score2 = score2 + points.get('C') + 3
        elif i == 'C' and j == 'Z':
            score2 = score2 + points.get('A') + 6

    return score2

x = getInput()
print(getInput())
print("Task1: ", task1(x))
print("Task2: ", task2(x))

