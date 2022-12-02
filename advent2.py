
Scores = {"AX" : 4, "AY": 8, "AZ": 3, "BX":1, "BY": 5, "BZ":9, "CX":7,"CY":2, "CZ":6}

Scores2 = {"AX" : 3, "AY": 4, "AZ": 8, "BX":1, "BY": 5, "BZ":9, "CX":2,"CY":6, "CZ":7}

def CalculateRPS(Lines):
    score = 0 
    for line in Lines:
        line = (line.strip()).replace(' ', '')
        score+= Scores2[line]
    return score 

if __name__ == '__main__':
    file1 = open("input2.txt", "r")
    Lines = file1.readlines()
    print(CalculateRPS(Lines))