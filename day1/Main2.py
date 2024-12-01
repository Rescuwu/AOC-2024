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


@timeit
def Part1():
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

    # adding distance to total
    for x in range(len(l1)):
        # abs to make sure its always positive
        Distance+=abs(l2[x]-l1[x])
    return Distance

def Part2():

    return None

if __name__ == "__main__":
    #answer printed
    print(Part1())
    