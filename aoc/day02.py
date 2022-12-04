

def getInput():
    with open("../../../AppData/Roaming/JetBrains/PyCharmCE2022.2/scratches/day02.txt", "r") as f:
        x = [list(i) for i in f.read().split('\n')]
    for i in x:
        i.remove(' ')
    return x

def findScore(x):
    points = {'A': 1, 'B': 2, 'C': 3}
    score = 0
    for i in x:
        for j in i:
            if j == 'A':
                if i[0] == 'X':
                    score = score + (points.get('A') * 2)
                elif j+1 == 'Y':
                    score = score + points.get('A')
                elif j+1 == 'Z':
                    score = score + points.get('A') + 6
            while j == 'B':
                if j+1 == 'X':
                    score = score + points.get('A') + 6
                elif j+1 == 'Y':
                    score = score + points.get('A') * 2
                elif i+1 == 'Z':
                    score = score + points.get('A')
            while i == 'C':
                if i+1 == 'X':
                    score = score + points.get('A')
                elif i+1 == 'Y':
                    score = score + points.get('A') + 6
                elif i+1 == 'Z':
                    score = score + (points.get('A')) * 2
    print(points)
    return score



print(getInput())
print(findScore(getInput()))