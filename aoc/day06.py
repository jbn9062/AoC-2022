import itertools
with open("day06.txt","r") as f:
    inpt = f.readline().strip()
input = []
for i in range(len(inpt)):
    input.append(inpt[i])

def window(x):
    wins = []
    for i in range(len(x)):
        wins.append(x[i:i + 4])
    return wins


def uniqWin(wins):
    for i in range(len(wins)):
        if len(wins[i]) == len(set(wins[i])):
            print("start = ", i+4," win= ", wins[i]) #i+4 to get the index of the last alphabet of the first hit.

uniqWin(window(input))
