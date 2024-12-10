
def filehandler():
    f=open("day6/input","r").read()
    return f

def Part1(s):
    l=s.strip().split("\n")
    for y in l:
        print("len_y:",len(y))
        print("y:",repr(y))
        for x in y:
                if len(x)!=1:
                    print("len_x:",len(x))
            #print("x:",x,"type:",type(x))
    D={}#to remember where it has been
    direction=0# 0 = up 1 = right 2 = down 3 = left
    y_len=len(l)
    currentpos=[0,0]#y x
    
    #find current position
    for y in range(y_len):
        x_len=len(l[y])
        for x in range(x_len):
            if "^"==l[y][x]:
                currentpos=[y,x]
                #print("Currentpos:",currentpos)
                #l[y][x]="."
                l[y]=l[y].replace("^",".")
                s_current=str(currentpos)
                break
        if currentpos!=[0,0]:
            break
    #loop over data and run around with char :3
    print("b4,while,pos:",currentpos)
    while True:
        if 0==direction: # up
            for y in range(currentpos[0]-1,-1,-1):
                #print("y",y)
                print("y:",y,"pos:,",currentpos)
                print("index:",l[y])
                if "."==l[y][currentpos[1]]:
                    if s_current not in D:
                        D[s_current]=0
                    D[s_current]+=1
                    #print("b4.asign,pos:",currentpos)
                    currentpos[0]=y
                    #print("0,pos:",currentpos)
                    s_current=str(currentpos)
                else:
                    direction+=1
                    break
        if 1==direction: # right
            for x in range(currentpos[1],len(l[currentpos[1]]),+1):
                if "."==l[currentpos[0]][x]:
                    if s_current not in D:
                        D[s_current]=0
                    D[s_current]+=1
                    currentpos[1]=x
                    s_current=str(currentpos)
                else:
                    direction+=1
                    break
        if 2==direction: # down
            for y in range(currentpos[0],y_len,+1):
                if "."==l[y][currentpos[1]]:
                    if s_current not in D:
                        D[s_current]=0
                    D[s_current]+=1
                    currentpos[0]=y
                    s_current=str(currentpos)
                else:
                    direction+=1
                    break
        if 3==direction: # left
            for x in range(currentpos[1],-1,-1):
                if "."==l[currentpos[0]][x]:
                    if s_current not in D:
                        D[s_current]=0
                    D[s_current]+=1
                    currentpos[1]=x
                    s_current=str(currentpos)
                else:
                    direction=0
                    break
        #print("Pos:",currentpos)
        if ((currentpos[0]==0) or (currentpos[0]==len(l)-1) or
            (currentpos[1]==0) or (currentpos[1]==len(l[currentpos[0]])-1)):
            print("currentpos:",currentpos)
            break
    return len(D)+1

if "__main__" == __name__:
    text=filehandler()
    print(Part1(text))