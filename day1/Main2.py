from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        #print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        print(f'Function {func.__name__}Took {total_time:.6f} seconds')
        return result
    return timeit_wrapper

def timeit100(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        Nyatime=0
        for x in range(100):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            Nyatime+=total_time
        Nyatime/=100
        #print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        print(f'Function {func.__name__}Took {Nyatime:.6f} seconds')
        return result
    return timeit_wrapper
#reads file and puts into list and returns
def filehandler():
     #vars
    l1=[]
    l2=[]
    Distance=0

    #Reading input
    f = open("input","r").readlines()
    for x in f:
        #splits it into a list 
        l=x.split()
        #appending to the lists and converting to int
        l1.append(int(l[0])),l2.append(int(l[1]))

    #sorts lists
    l1.sort(),l2.sort()
    return l1,l2

@timeit
def Part1():
    #vars
    Distance=0
    l1,l2 = filehandler()

    # adding distance to total
    for x in range(len(l1)):
        # abs to make sure its always positive
        Distance+=abs(l2[x]-l1[x])
    return Distance

@timeit
def Part2():
    #vars
    total=0
    l1,l2 = filehandler()

    for x in l1:
        k=0
        for y in l2:
            if x==y:
                k+=y
            elif x<y:
                break
        total+=k
    return total

if __name__ == "__main__":
    #answer printed
    print(Part1())
    print(Part2())
    