with open("day04.txt", "r") as f:
    file = f.read().split("\n")
    input = [i.split(",") for i in file]
    input2 = [[j.split("-") for j in i] for i in input]
print(input2)

for i in input2:
    for j in i:
        for ji in j:
            ji = int(ji)
print(input2)

nums = []
for i in input2:
    temp = []
    for j in i:
        for ji in j:
            temp.append(int(ji))
    nums.append(temp)
print(nums)
temp = []
part1 = 0
for i in nums:
    start1 = i[0]
    end1 = i[1]
    start2 = i[2]
    end2 = i[3]
    if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
        part1 += 1
print("part1: ",part1)

######################PART 2#################################################
part2 = 0
for i in nums:
    start1 = i[0]
    end1 = i[1]
    start2 = i[2]
    end2 = i[3]
    if (start1 in range(start2, end2 +1)) or (end1 in range(start2, end2+1)):
        part2 = part2 + 1
    elif (start2 in range(start1, end1 + 1)) or (end2 in range(start1, end1 +1)):
        part2 = part2 + 1
print("part2: ",part2)
