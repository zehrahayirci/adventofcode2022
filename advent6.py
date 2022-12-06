
def CalculateMarker(Lines,count):
    chars = Lines[0]
    for i,c in enumerate(chars): 
        print(i, " " ,c)
        fourBlock = chars[i:i+count]
        print(fourBlock)
        fourBlock = list(set(fourBlock))
        print(fourBlock)
        if len(fourBlock) == count:
            return i+count

if __name__ == '__main__':
    file1 = open("input6.txt", "r")
    Lines = file1.readlines()
    print(CalculateMarker(Lines,14))