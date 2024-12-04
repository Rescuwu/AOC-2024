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

def Part2():
    l1=filehandler()

    condition = {
        "safe" : 0,
        "unsafe" : 0,
        "orderreverse" : 0,
        "order" : 0
    }
    f=open("unsafe","a")
    #function for checking input to see if problems are 2 or less :3
    #only take increasing order
    def checkinput(l1,safe=2):
        #safe=2
        y=l1[0]
        z=l1[1]
        for z in range(1,len(l1)):
            z=l1[z]
            #if ((z-y>3) or (z-y<=0)):
            if ((y-z>3) or (y-z<=0)):
                safe-=1
                if not safe:
                    #break
                    return False
            else:
                y=z
                #print("test")
        return True
    def checkinput2(l1,safe=2):
        #safe=2
        y=l1[0]
        z=l1[1]
        for z in range(1,len(l1)):
            z=l1[z]
            #if ((z-y>3) or (z-y<=0)):
            if ((y-z>3) or (y-z<=0)):
                safe-=1
                if not safe:
                    #break
                    return False
                if l1[0]==y:
                    y=z
            else:
                y=z
                #print("test")
        return True

    #Checking order if increasing or decreasing
    for x in l1:
        order=0
        for y in range(4):
            for z in range(y,4):
                if y==z:
                    pass
                else:
                    i=x[y]-x[z]
                    if i>0: # positive order aka doesnt need to reverse it
                        order+=1
                    elif i<0: # negative order aka needs reversing
                        order-=1
        #print(order)
        if 0>order:
            x.reverse()
            condition["orderreverse"]+=1
        if checkinput(x):
            condition["safe"]+=1
        elif checkinput2(x):
            condition["safe"]+=1
        else:
            condition["unsafe"]+=1
            #print("unsafe: ",end="")
            #print(x)
            #f.write(' '.join(map(str,x))+"\n")
    return condition

        

    
"""
def Part2():
    l1=filehandler()
    
    safe=2# if 0 or less aka false, means there was more than 1 problem.
    condition={
        "safe" : 0,
        "unsafe" : 0
    }
    for x in l1[:]:
        safe=2
        y=x[0]
        z=x[1]
        if y>z:
            for _z in range(1,len(x)):
                z=x[_z]
                if ((y-z>3) or (y-z<=0)):
                    condition["unsafe"]+=1
                    safe-=1
                    if not safe:
                        break

                else:
                    y=z
        
        elif y<z: # increasing
            for _z in range(1,len(x)):
                z=x[_z]
                if ((z-y>3) or (z-y<=0)):
                    condition["unsafe"]+=1
                    safe-=1
                    if not safe:
                        break
                else:
                    y=z

        elif y==z:
            condition["unsafe"]+=1
            safe-=1
            y=x[1]
            z=x[2]
            if y>z:
                for _z in range(2,len(x)):
                    z=x[_z]
                    if ((y-z>3) or (y-z<=0)):
                        condition["unsafe"]+=1
                        safe-=1
                        break

                    else:
                        y=z
            
            elif y<z: # increasing
                for _z in range(2,len(x)):
                    z=x[_z]
                    if ((z-y>3) or (z-y<=0)):
                        condition["unsafe"]+=1
                        safe-=1
                        break
                    else:
                        y=z
            elif y==z:
                safe-=1
                #break # broke part2
            else:
                print("wut")
        if safe:
            condition["safe"]+=1
    return condition
"""

if "__main__" == __name__:
    #data=Part1()
    #print(data["safe"])
    data=Part2()
    for x in data.keys():
        print(x,data[x])