import re

def filehandler():
     #vars
    s=""

    #Reading input
    f = open("day3/input","r").readlines()
    for x in f:
        s+=x

    return s

def Part1(s):
    total=0
    #find=re.findall("mul\(\d{1,3},\d{1,3}\)",s)
    find=re.findall("mul\\(\\d{1,3},\\d{1,3}\\)",s)
    for x in find:
        y=x.replace("mul(","").replace(")","").split(",")
        total+=int(y[0])*int(y[1])

    return total

def Part2(s):
    total=0
    #/(do\(\))|(don't\(\))|(mul\(\d{1,3},\d{1,3}\))/g
    find=re.findall("do\\(\\)|don't\\(\\)|mul\\(\\d{1,3},\\d{1,3}\\)",s)
    #print(find)
    count=True
    for x in find:
        if x.startswith("mul"):
            if count:
                y=x.replace("mul(","").replace(")","").split(",")
                total+=int(y[0])*int(y[1])
        elif x.startswith("do()"):
            count=True
        elif x.startswith("don't()"):
            count=False
        else:
            print("wut")

    return total
if "__main__" == __name__:
    p1_total=0
    p2_total=0
    filetext=filehandler()
    p1_total=Part1(filetext)
    print("Part1: ", p1_total)
    p2_total+=Part2(filetext)
    print("part2: ", p2_total)