#exercise1
from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000):  #keep going and removes from memory
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000)):  #the list store in memory and keep going
        i * 5


long_time()  #much faster
long_time2()





#exercise2 (Fibonacci numbers)
#create a function that takes a number and the number is going to be


def fib(number):
    a = 0  #f0
    b = 1  #f1
    for i in range(number):
        yield a
        x = a  #x = 0, x = 1
        a = b  #a = 1, a = 1
        b = x + b  #b = 0+1, b = 1+1


for item in fib(20):
    print(item)


#in a list
def fib2(number):
    a = 0  #f0
    b = 1  #f1
    result = []
    for i in range(number):
        result.append(a)
        x = a  #x = 0, x = 1
        a = b  #a = 1, a = 1
        b = x + b  #b = 0+1, b = 1+1
    return result


print(fib2(8))






#Example 1
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)
                  )  #next functions is going to output whatover the item is
        except StopIteration:
            break


special_for([1, 2, 3])






#Example2
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = self.first  #this line allows us to use the current number as the starting point for the iteration

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:  #need to have some sort of state or data to keep track of where we are
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)
for i in gen:
    print(i)
