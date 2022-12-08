"""values as constants
A,X = rock -> 1 points
B,Y = paper -> 2 points
C,Z = scissors -> 3 pionts
A,B,C = you
lose = X  
draw = Y
win = Z"""

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

elementsWin = {
    "A": "B", 
    "B":  "C",
    "C": "A"
}

elementsLose = {
    "A" : "C", 
    "B" : "A",
    "C" : "B"
}
wins = ["AB","BC", "CA"]


def process_file(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
            roundValue = 0
            oponent, final = line.split()
            if final == "Y":
                me = oponent
                roundValue =+3
            elif final == "X":
                me = elementsLose[oponent]
            else:
                me = elementsWin[oponent]
                roundValue =+ 6
            roundValue += elementScores[me]
#            print(roundValue)
            result += roundValue
    return result
        

               

#            print(oponent,me)
    
if __name__ == "__main__":
#    print("Hello")
#    process_file(FILE_NAME)
    result = process_file(FILE_NAME)
    print(result)