import math
class Monkey:
    def __init__(self, monk):
        self.monk = monk
        self.mk_st = [int(i) for i in monk['Starting items'].split(', ')]
        self.mk_oper = [int(i) if i.isnumeric() else i for i in monk['Operation'].split()]
        self.mk_test = [int(i) if i.isnumeric() else i for i in monk['Test'].split()]
        self.true = [int(i) if i.isnumeric() else i for i in monk['If true'].split()]
        self.false = [int(i) if i.isnumeric() else i for i in monk['If false'].split()]

    def mult(self, old):
        self.old = old
        self.new = old * self.mk_oper[-1]
        return self.new

    def add(self, old):
        self.old = old
        self.new = old + self.mk_oper[-1]
        return self.new

    def test(self, item):
        self.item = item
        self.div = self.mk_test[-1]
        return item % self.div == 0

    def lesswry(self, item):
        self.item = item
        return item // 3

    def if_true(self, result):
        if result == True:
            pass



with open("day11.txt", "rt") as f:
    data = [i.strip("\n") for i in f.readlines()]

mnky0 = data[:6]
mnky1 = data[7:13]
mnky2 = data[14:20]
mnky3 = data[21:27]
mnky4 = data[28:34]
mnky5 = data[35:41]
mnky6 = data[42:48]
mnky7 = data[49:]


monk0 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky0}
monk1 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky1}
monk2 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky2}
monk3 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky3}
monk4 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky4}
monk5 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky5}
monk6 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky6}
monk7 = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in mnky7}

m0 = Monkey(monk0)
m1 = Monkey(monk1)
m2 = Monkey(monk2)
m3 = Monkey(monk3)
m4 = Monkey(monk4)
m5 = Monkey(monk5)
m6 = Monkey(monk6)
m7 = Monkey(monk7)

def part1():
    counts = [0, 0, 0, 0, 0, 0, 0,0]
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]
    for round in range(20):

        for i in range(len(monkeys)):

            for j in range(len(monkeys[i].mk_st)):
                counts[i] += 1

                if '*' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == int:

                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] * monkeys[i].mk_oper[-1]
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3

                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)


                if '*' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == str:
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] * monkeys[i].mk_st[0]
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3


                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)


                if '+' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == int:
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] + monkeys[i].mk_oper[-1]
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3


                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)



                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)


                if '+' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == str:
                    monkeys[i].mk_st[j] = monkeys[i].mk_st[j] + monkeys[i].mk_st[j]
                    monkeys[i].mk_st[j] = monkeys[i].mk_st[j] // 3


                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        j = len(monkeys[i].mk_st)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        j = len(monkeys[i].mk_st)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)


    return (sorted(counts)[-1] * sorted(counts)[-2])

#print(part1())

def part2():
    counts = [0, 0, 0, 0, 0, 0, 0, 0]
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]
    for round in range(10000):

        for i in range(len(monkeys)):

            for j in range(len(monkeys[i].mk_st)):
                counts[i] += 1

                if '*' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == int:

                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] * monkeys[i].mk_oper[-1]
                    #monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3

                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)

                if '*' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == str:
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] * monkeys[i].mk_st[0]
                    #monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3

                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)

                if '+' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == int:
                    monkeys[i].mk_st[0] = monkeys[i].mk_st[0] + monkeys[i].mk_oper[-1]
                    #monkeys[i].mk_st[0] = monkeys[i].mk_st[0] // 3

                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)



                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)

                if '+' in monkeys[i].mk_oper and type(monkeys[i].mk_oper[-1]) == str:
                    monkeys[i].mk_st[j] = monkeys[i].mk_st[j] + monkeys[i].mk_st[j]
                    #monkeys[i].mk_st[j] = monkeys[i].mk_st[j] // 3

                    if monkeys[i].test(monkeys[i].mk_st[0]) == True:
                        throw = monkeys[i].mk_st.pop(0)
                        j = len(monkeys[i].mk_st)
                        monkeys[monkeys[i].true[-1]].mk_st.append(throw)


                    elif monkeys[i].test(monkeys[i].mk_st[0]) == False:
                        throw = monkeys[i].mk_st.pop(0)
                        j = len(monkeys[i].mk_st)
                        monkeys[monkeys[i].false[-1]].mk_st.append(throw)
    return (sorted(counts)[-1] * sorted(counts)[-2])