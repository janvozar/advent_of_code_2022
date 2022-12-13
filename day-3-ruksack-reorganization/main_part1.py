FILE_NAME = "input.txt"

def read_file(file_name):
    result = []
    with open(file_name,"r") as f:
        for line in f:
            result.append(line.strip())
    return result

def process_bags(bags):
    result = 0
    for bag in bags:
        #result += process_bag(bag)
        #print(process_bag(bag))
        result += encode_char(process_bag(bag))
    return result 

def process_bag(bag):
    middle = int(len(bag)/2)
    for e in bag[:middle]:
        if e in bag[middle:]:
            return e

def encode_char(charc):
    if ord(charc) >= ord('a'):
        return ord(charc) - ord('a') + 1
    else:
        return ord(charc) - ord('A') + 27 

if __name__ == "__main__":
#   print("Hello")
#   print(read_file(FILE_NAME))
    bags = (read_file(FILE_NAME))
    #process_bags(bags)
    print(process_bags(bags))
