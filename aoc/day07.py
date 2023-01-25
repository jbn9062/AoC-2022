import pprint

with open("day07.txt", "rt")as f:
    data = f.read().strip().split("\n")

folders = {"/": 0}
stack = ["/"]
visited = set()

for i in range(len(data)):
    cmds = data[i].split(" ")
    if cmds[0] == '$':
        if cmds[1] == 'cd':
            if cmds[2] == '/':
                stack = ["/"]

            elif cmds[2] == "..":
                stack.pop()

            else:
                if cmds[2] != ".." and cmds[2] != "/":
                    if stack[-1] != "/":
                        stack.append("/" + cmds[2])
                    else:
                        stack.append(cmds[2])
                    path = "/".join(stack)
                    if path not in visited:
                        visited.add(path)
                        folders[path] = 0

        elif cmds[1] == "ls":
            pass

    elif cmds[0] == "dir":
        pass

    elif cmds[0].isnumeric():
        size = int(cmds[0])
        if stack[-1].isnumeric():
            stack.pop()
        path = "/".join(stack)
        folders[path] += size

# Find all directories with a total size of at most 100000
dirs_size_le_100000 = [dir for dir, size in folders.items() if size <= 100000]

# Calculate the sum of the total sizes of those directories
total_size = sum(folders[dir] for dir in dirs_size_le_100000)
print(total_size)
