from itertools import accumulate

FILE_NAME="test_input.txt"

def process_input(input):
    res = 0
    for i, row in enumerate(input):
        for j, _ in enumerate(row):
            if proces_tree(i, j, input, len(input)):
                res+=1
    return res

def proces_tree(row, column, input, max_size):
    directions = ["r","l","u","d"]
    for i in range(1, max_size):
        tmp_directions = directions.copy()
        for direction in tmp_directions:
            if direction == "r":
                if column + i == max_size:
                    return True
                elif input[row][column] <= input[row][column + i]:
                    directions.remove(direction)
           
            if direction == "l":
                if column - i < 0:
                    #==-1
                    return True
                elif input[row][column] <= input[row][column - i]:
                    directions.remove(direction)
            
            if column == "d":
                if row + i == max_size:             
                    return True
                elif input[row][column] <= input[row + i][column]:
                    directions.remove(direction)

            if column == "u":
                if row - i < 0:             
                    return True
                elif input[row][column] <= input[row - i][column]:
                    directions.remove(direction)

        if not len(directions):
             return False
    return False


def proces_file(filename):
    res = []
    with open(FILE_NAME) as f:
        for line in f.readlines():
            res.append(list([int(x) for x in line.strip()]))
    return res


if __name__== "__main__":
    input = proces_file(FILE_NAME)
    #print(input)
    print(process_input(input))