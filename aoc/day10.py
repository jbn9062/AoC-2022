with open("day10.txt", "rt") as f:
    data = [i.split() for i in f.readlines()]

for i in data:
    if len(i) == 1:
        i.append(0)


d_list = [{i[0]: int(i[1])} for i in data]
print(f"{len(d_list)} : {d_list}\n")


cycles = [20, 60, 100, 140, 180, 220] #  @ 20: x = 21 st = 420
x = 1
cycle = 0
signalStrength = 0

for i in d_list:
    if 'noop' in i.keys():
        cycle += 1
        if cycle in cycles:
            signalStrength += (x * cycle)
            print(f"signal strength: {signalStrength} in the {cycle}th cycle")



    elif 'addx' in i.keys():
        c = 2
        while c > 0:
            cycle += 1

            if cycle in cycles:
                signalStrength += (x * cycle)
                print(f"signal strength: {signalStrength} in the {cycle}th cycle")
            c = c - 1
        x += i['addx']
print(x)
print(cycle)
print(signalStrength)