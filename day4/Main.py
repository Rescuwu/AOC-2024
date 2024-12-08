from mylibs.utils import *


def filehandler():
    f=open("day4/input","r").read()
    return f


Search=[
        "XMAS",
    ]
def Part1_pattern_return():
    a=[]
    #print(len(Search))
    if len(Search)==1:
        return Part1_pattern_cords(Search[0])
    for name in Search:
        a.append(Part1_pattern_cords(name))
    return a


def Part1_pattern_cords(s,y=0,x=0):
    l=[]
    for i in range(-1,2):
        for j in range(-1,2):
            if i==j:
                #continue
                pass
            if ((0==i) and (0==j)):
                continue
            temp=[]
            for k in range(len(s)):
                temp.append([y+k*i,x+k*j])
            l.append(temp)
    return l

@timeit
def Part1(s):
    countbreak={}
    d={}
    d["XMAS"]=Part1_pattern_return()
    sum=0
    a=s.split("\n")[:-1]
    #print(repr(a[]))
    #return
    len_y=len(a)
    for y in range(len_y):
        len_x=len(a[y])
        for x in range(len_x):
            for key in d:
                for cords in d[key]:
                    for count,cord in enumerate(cords):
                        #print(count,cord)
                        cord_y, cord_x = y+cord[0],x+cord[1]
                        if ((cord_y<0) or (cord_x<0) or (cord_y>=len_y) or (cord_x>=len_x)):
                            break
                        #print(cord_y,cord_x,a[cord_y][cord_x],count)
                        #print(cord_x,len_x,cord_y,len_y, a[y])
                        if not a[cord_y][cord_x]==key[count]:
                            break
                        if count==len(key)-1:
                            sum+=1

    return sum


def Part2(s):
    sum=0
    a=s.strip().split()
    len_y=len(a)
    for y in range(1,len_y-1):
        len_x=len(a[y])
        for x in range(1,len_x-1):
            if a[y][x]=="A":
                """
                1M.M
                .A.
                S.S
                """
                if a[y-1][x-1]=="M":
                    if (a[y+1][x-1]=="M"):
                        if ((a[y-1][x+1]=="S")and(a[y+1][x+1]=="S")):
                            sum+=1
                    elif a[y-1][x+1]=="M":
                        if ((a[y+1][x-1]=="S")and(a[y+1][x+1]=="S")):
                            sum+=1
                elif a[y+1][x+1]=="M":
                    if (a[y+1][x-1]=="M"):
                        if ((a[y-1][x+1]=="S")and(a[y-1][x-1]=="S")):
                            sum+=1
                    elif a[y-1][x+1]=="M":
                        if ((a[y+1][x-1]=="S")and(a[y-1][x-1]=="S")):
                            sum+=1

    return sum


if "__main__" == __name__:
    text=filehandler()
    #Part1(text)
    #print(Part1(text))
    print(Part2(text))
    #print(Part1_pattern_return())
    #print(Part2_pattern_cords())
    for x in Part1_pattern_return():
        break
        print(x)
