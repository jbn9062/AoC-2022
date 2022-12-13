with open("day06.txt","r") as f:
    inpt = f.readline().strip()
input = []
for i in range(len(inpt)):
    input.append(inpt[i])

def window1(x):
    wins = []
    for i in range(len(x)):
        wins.append(x[i:i + 4])
    return wins

wins = window1(input)

def part1(wins):
    for i in range(len(wins)):
        if len(wins[i]) == len(set(wins[i])):
            if len(wins[i]) > 3:
                print("start = ", i+4," win= ", wins[i]) #i+4 to get the index of the last alphabet of the first hit.

part1(wins)


def window2(x):
    wins2 = []
    for i in range(len(x)):
        wins2.append(x[i:i + 14])
    return wins2


wins2 = window2(input)

def part2(wins2):
    for i in range(len(wins2)):
        if len(wins2[i]) == len(set(wins2[i])):
            if len(wins2[i]) > 13:
                print("\n\nstart = ", i+14," win2= ", wins2[i])

part2(wins2)
