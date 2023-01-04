import string
import itertools
with open("day12.txt", "rt") as f:
    data = [line.strip().split() for line in f.readlines()]
print(data)

alphabets = dict(zip(string.ascii_lowercase, range(1, 27)))
alphabets['S'] = 0
alphabets['E'] = 28
print(alphabets)
count = 0


for row in range(len(data)):
    for col in range(len(data[row])):
        if :
            left = data[row][col-1]
            right = data[row][col+1]
            up = data[row-1][col]
            down = data[row+1][col]



