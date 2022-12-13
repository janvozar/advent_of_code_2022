"""values as constants
A,X = rock -> 1 points
B,Y = paper -> 2 points
C,Z = scissors -> 3 pionts
A,B,C = you
X,Y,Z = opponent
outcome of round
win =  6 points  
lose = 0 points
draw = 3 points"""

FILE_NAME = "input.txt"

elementMapping = {
   "X": "A",
   "Y": "B",
   "Z": "C"  
}


elementScores = {
    "A": 1,
    "B": 2,
    "C": 3
}

wins = ["AB","BC", "CA"]


def process_file(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
#            print(line)
            oponent, encoded_me = line.split()
            me = elementMapping[encoded_me]
            play = oponent + me
            roundValue = 0
            if oponent == me:
                roundValue += 3
            elif play in wins:
                roundValue += 6
            roundValue += elementScores[me]
            result += roundValue
        return result       

#            print(oponent,me)
    
if __name__ == "__main__":
#    print("Hello")
#    process_file(FILE_NAME)
    result = process_file(FILE_NAME)
    print(result)
