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
count = 0
for i in nums:
    start1 = i[0]
    end1 = i[1]
    start2 = i[2]
    end2 = i[3]
    if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
        count += 1
print(count)