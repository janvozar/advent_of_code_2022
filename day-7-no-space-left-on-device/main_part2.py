from itertools import accumulate
FILE_NAME = "input.txt"

if __name__ == "__main__":
    stack = []
    folder_sizes = {}
    with open(FILE_NAME) as f:
        for line in f:
            if line.startswith("$ ls") or line.startswith("dir"):
                continue
            parts = line.split()
            #instead of lot of if match case in Pyhon 3.10
            if line == "$ cd ..\n":
                stack.pop()
            elif line.startswith("$ cd"):
                stack.append(parts[2])
            else:
               #print(parts[0])
            # Python function accumulate from library itertools
            # from itertools import accumulate
                for folder in accumulate(stack, lambda x,y: x + "_" + y):
                    if folder not in folder_sizes.keys():
                        folder_sizes[folder] = 0
                    value = folder_sizes.get(folder, 0)
                    folder_sizes[folder] += int(parts[0])
    #print(folder_sizes)
    #print(sum(filter(lambda x: x < 100000, folder_sizes.values())))
    print(min(filter(lambda x: folder_sizes["/"] - 40000000 <= x, folder_sizes.values())))      