Distance=0
l1=[]
l2=[]

#Reading input
with open("input","r") as f:
    for x in f:
        #splits it into a list 
        l=x.split()
        #appending to the lists and converting to int
        l1.append(int(l[0])),l2.append(int(l[1]))

#sorts lists
l1.sort(),l2.sort()

# adding distance to total
for x in range(len(l1)):
    # abs to make sure its always positive
    Distance+=abs(l2[x]-l1[x])

#answer printed
print(Distance)