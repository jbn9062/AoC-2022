
def get_input():
    with open("day01.txt", "r") as f:
        x = f.read().split('\n\n')
        x = [i.split('\n') for i in x]
    return x
x = get_input()

def calc_find(x):
    total = []
    for i in x:
        tot = 0
        for j in i:
            tot = tot + int(j)
            total.append(tot)
    print(max(total))
    return total

calories = calc_find(x)

def topThree(calories):
    calories.sort()
    return sum(calories[-3:])
print(calc_find(x))
print(topThree(calories))





