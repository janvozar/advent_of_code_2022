FILE_NAME = "input.txt"

def process_line(line):
    sections = line.split(",")
    process_sections = list(map(lambda x: x.split("-"),sections)) 
    #return sections
    #return [sections[0].split("-"), sections[1].split("-")]
    #return list(map(lambda x: x.split("-"), sections))
    #return ([process_sections[0][0], process_sections[0][1]]) 
    result = []
    for s in process_sections:
        result.append([int(s[0]), int(s[1])])
    return result

def contains(s1,s2):
    if s2[0] >= s1[0] and s2[1] <= s1[1]:
        return True
    return False

def overlaps(s1, s2):
    if s1[0] <= s2[1] and s1[1] >= s2[1]:
        return 1
    if s1[0] <= s2[0] and s1[1] >= s2[0]:
        return 1   

def read_file(file_name):
    result = []
    with open(file_name, "r") as f:
        for line in f:
            result.append(process_line(line.strip()))
    return result

def read_file(file_name):
    result = []
    with open(file_name, "r") as f:
        for line in f:
            result.append (process_line(line.strip()))
    return result

def process_groups(groups):
    result = 0
    for group in groups:
        if contains(group[0], group[1]) or contains(group[1], group[0]):
            #print(group)
            result+=1
    return result

def process_groups2(groups):
    result = 0
    for group in groups:
        if overlaps(group[0], group[1]) or overlaps(group[1], group[0]):
            result+=1
    return result

if __name__ == "__main__":
    #print("Hello")
    #print(read_file(FILE_NAME))
    cleaning_groups = read_file(FILE_NAME)
    #process_groups(cleaning_groups)
    #print(process_groups(cleaning_groups))
    print(process_groups2(cleaning_groups))