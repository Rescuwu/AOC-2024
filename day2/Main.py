from mylibs.utils import *
import os


def filehandler():
     #vars
    l1=[]

    #Reading input
    f = open("day2/input","r").readlines()
    for x in f:
        #splits it into a list 
        l=list(map(int, x.split()))
        #appending to the lists and converting to int
        l1.append(l)

    return l1

def Part1():
    l1=filehandler()
    
    safe=1
    condition={
        "safe" : 0,
        "unsafe" : 0
    }
    for x in l1[:]:
        safe=1
        y=x[0]
        z=x[1]
        if y>z:
            for _z in range(1,len(x)):
                z=x[_z]
                if ((y-z>3) or (y-z<=0)):
                    condition["unsafe"]+=1
                    safe=0
                    break

                else:
                    y=z
        
        elif y<z: # increasing
            for _z in range(1,len(x)):
                z=x[_z]
                if ((z-y>3) or (z-y<=0)):
                    condition["unsafe"]+=1
                    safe=0
                    break

                else:
                    y=z

        elif y==z:
            condition["unsafe"]+=1
            safe=0
        if safe:
            condition["safe"]+=1
    return condition


if "__main__" == __name__:
    data=Part1()
    print(data["safe"])