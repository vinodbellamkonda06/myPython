#In Python, anonymous function means that a function is without a name.
#  As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
# It has the following syntax:lambda arguments: expression
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y;


g = lambda x: x * x * x
print(g(7))

print(cube(5))
#Use of lambda() with filter()

#The filter() function in Python takes in a function and a list as arguments.
#  This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
# Here is a small program that returns the odd numbers from an input list:
# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)
#Use of lambda() with map()

#The map() function in Python takes in a function and a list as argument.
# The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item. Example:
# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)
#Use of lambda() with reduce()

#The reduce() function in Python takes in a function and a list as argument.
# The function is called with a lambda function and a list and a new reduced result is returned.
# This performs a repetitive operation over the pairs of the list. This is a part of functools module. Example:

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


'''s = lambda x:x **2
print(s(3))
d = map(lambda x:x*2,li)
print(d.__next__())
print(list(d))
#print(d.__next__())
A = filter(lambda x:x%2==0,li)

print(A.__next__())
print(A.__next__())'''

