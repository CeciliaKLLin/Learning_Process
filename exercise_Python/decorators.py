#performance decorator.
from time import time  #this is module


#create the decorator
def performance(fn):
    def wrapper(*args, **kwargs):
        #calculate the beginning of running the functions to the end
        t1 = time()  #start a time, this initial time
        result = fn(*args, **kwargs)
        t2 = time()  #the end time
        print(f'took {t2-t1}')  #the calculation
        return result

    return wrapper


#use to test how fast the code runs
@performance
def long_time():
    for i in range(10000):
        i * 5


long_time()




