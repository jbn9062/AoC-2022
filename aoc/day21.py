from sympy import parse_expr
with open("day21.txt", "rt") as f:
    content = f.read().strip().split("\n")

data = dict()
for i in content:
    key = i.split(":")[0].strip()
    value = i.split(":")[1].strip()
    data[key] = value

print(content)
yells = dict()
for task in content:
    key, value = task.split(": ")
    if value.isnumeric():
        yells[key] = int(value)

    else:
        num1, op, num2 = value.split()
        if num1 in yells and num2 in yells:
            yells[key] = parse_expr(str(yells[num1]) + op + str(yells[num2]))

        else:
            content.append(task)

print(yells["root"])


##  Reference

##  https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day21p1.py
