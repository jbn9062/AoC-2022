

def getInput():
    with open("day02.txt", "r") as f:
        x = [list(i) for i in f.read().split('\n')]
    for i in x:
        i.remove(' ')
    return x

def findScore(x):
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for i in x:
        for j in i:
            if j[0] == 'A':
                print(j[-1])
                score = points['A'] + points['X']
                print(score)
            elif j[0] == 'A' and j[-1] == 'Y':
                score = score + points.get('A')
            elif j[0] == 'A' and j[-1] == 'Z':
                score = score + points.get('A') + 6
    print(points)
    return score

x = getInput()
print(getInput())
print(findScore(x))

#********************TEST********************
'''def test_findScore():
    y = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    assert findScore(y) == 15'''