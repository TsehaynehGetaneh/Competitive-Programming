def countingValleys(steps, path):
    # Write your code here
    seeLevel = 0
    valleys = 0
    for i in range(len(path)):
        if path[i] == "U":
            seeLevel +=1
        else:
            if seeLevel == 0:
                valleys +=1
            seeLevel -=1
    return valleys