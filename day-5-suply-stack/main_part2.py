FILE_NAME = "input.txt"

def move_crate(stacks, moves):
    for move in moves:
        moving = stacks[move[1]][:move[0]]
        #for c in moving:
        #stacks[move[2]] = [c] + stacks[move[2]]
        stacks[move[2]] = moving + stacks[move[2]]
        stacks[move[1]] = stacks[move[1]][move[0]:]
    return stacks

def process_file(filename):
    stacks = {}
    moves = []
    #it is better to create classes
    with open(filename, "r") as f:
        for line in f:
            #function for every if
            if line == "\n" or line[1] == "1":
                continue
            if not line.startswith("m"):
                for stack, crate in enumerate(range(1, len(line), 4)):
                    if line[crate] != " ": 
                    #print(line[crate], end=" ")
                        current_stack = stacks.get(stack +1, [])
                        stacks[stack + 1] = current_stack + [line[crate]]
            #print()
            if line.startswith("m"):
                parts = line.split()
                moves.append([int(parts[1]), int(parts[3]), int(parts[5])])
    return stacks, moves

if __name__ == "__main__":
    #process_file(FILE_NAME)
    stacks, moves = process_file(FILE_NAME)
    print(stacks)
    print(moves)
    stacks = move_crate(stacks, moves)
    print(stacks)
    result = ""
    for i in range(1, len(stacks.keys()) + 1):
        result += stacks[i][0]
    print(result)
