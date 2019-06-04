'''
POlymorphism:
    when a variable,object or method exibits different behavior in different forms\contexts.
Types of polymorphism:
    1.operator overloading
    2.method overloading
    3.method overriding
1.operatoe overloading:
    >>operator is a symbol which performs some action.
    >>To achive operator overloading in python we have to override the magic method of the particular operator.
    >>For example add have magic method __add__().When ever we call add internally this method will comes into picture.
    >>Every operator having its own magical method.
    >>to achive operatoe overloading we are fourcefully adding an extra task to the particular operator.
2.Method overloading:
    Normally method overloading is not avaliable in python.
         Method overloading is defined as if  a class having two or more methods with
    same name but different arguments.
    >>This can be achived by using *args,**kwargs

'''

#program to overloading the greaterthan operator
class Ramayan:
    def __init__(self,pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages


class Mahabarata:
    def __init__(self,pages):
        self.pages = pages


p1 = Ramayan(1000)
p2 = Mahabarata(1500)

if p1 > p2:
    print("Ramayana has more pages:")
else:
    print("Mahabarata has more pages:")


#program to overloading the add operator

class Ramayana:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


class Mahabarata:
    def __init__(self, pages):
        self.pages = pages


p1 = Ramayana(1000)
p2 = Mahabarata(1500)

print("sum of pages in ramayana and mahabarata is:", p1+p2)


# program to understand method overloading

class A:
    def add(self, *args):
        sum = 0
        for i in args:
            sum += i
        print("sum of given numbers is", sum)

obj = A()
obj.add(10, 20, 30)
obj.add(20, 40, 50, 90,)
obj.add()

import re
s = "hi this is vinod kumar my num is 9177000945 9247762033 vinodbellamkonda06@gmail.com"
print(re.findall(r"[0-9]+", s))
print(re.findall(r"\w+@\w+.\w+", s))


with open(r"C:\Users\Jagadeesh\Desktop\detail.txt", "r") as d1:
    data = d1.read()
    print(re.search(r"[0-9]+", data))


l = {1,2,3,4,5,6,7,8,9,10,23}
l1 = {i for i in l if i % 2 == 0}
print(l1)

for i in l:
    if i % 2 == 0:
        l1.append(i)


