#lambda exercise
my_list = [5, 4, 3]

#square
print(list(map(lambda item: item**2, my_list)))

#List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print((sorted(a, key=lambda tuple: tuple[1])))
#/
a.sort(key=lambda x: x[1])
print(a)

#comprehension exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicate = list(
    set([char for char in some_list if some_list.count(char) > 1]))
print(duplicate)

#Error Handling
while True:
    try:
        age = int(input('What is your age?'))
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I am finally done')
    print('can you hear me?')


#create a generator
def generator_function(num):
    for i in range(num):
        yield i
        #yield: pause the function and later come back to it when we call the function(next())


#if it has a yield keyword, it becomes a generator
#it only keep the most recent data in memory

for item in generator_function(1000):
    print(item)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

import re

pattern = re.compile('this')
string = 'search inside of this text please'
print('search' in string)
#a simple way to search string

a = re.search('this', string)
print(a)
print(a.span())  #index of (17,21) tell where the string occur as a tuple
print(a.start())  #tell where the text starts
print(a.end())  #tell where it ends
print(a.group())
b = pattern.search(string)
c = pattern.findall(string)
print(b)
print(c)

email_pattern = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_input = 'cecee68@gmail.com'
f = email_pattern.search(email_input)
print(f)

#enumerate()
#used when you need the index counter of the item
#index, interable object
for i, char in enumerate("Helloooo"):
    print(i, char)

for i, char in enumerate(list(range(20))):
    #want to be told what the index of the number 10 is
    if char == 10:
        print(f'the index of the number 10 is {i}')
    print(i, char)
