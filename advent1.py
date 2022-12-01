
def countCalories(Lines):
    maxCal = 0
    count = 0
    for line in Lines:
        if line.strip():
            count += int(line)
        else:
            if count > maxCal:
                maxCal = count
            count = 0
        #print(line," ",count," ",maxCal) 
    return maxCal
            
def countTopThreeCalories(Lines):
    ElfCalories = []
    count = 0
    for line in Lines:
        if line.strip():
            count += int(line)
        else:
            ElfCalories.append(count)
            count = 0 
    ElfCalories.sort()
    ElfCalories.reverse()
    return sum(ElfCalories[0:3])


if __name__ == '__main__':
    file1 = open("input1.txt", "r")
    Lines = file1.readlines() 
    print(countCalories(Lines))
    print(countTopThreeCalories(Lines))

