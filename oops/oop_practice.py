"""
oops concept is programing style associated with class and object.In this concept we can see the
  the concepts like
  1.INHERITENCE
  2.POLYMORPHISM
  3.ENCAPSULATION
  4.ABSTRACTION
"""
from abc import abstractmethod, ABC

# Inheritence bellamkondavinod06@gmail.com


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name :", self.name)
        print("age :", self.age)


class Men(Person):
    pass


m1 = Person("vinod", 23)
m1.display()


class Women(Person):
    pass


w1 = Women("shobha", 23)
w1.display()

# Example for understanding operator overloading


class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __add__(self, other):
        print(self.pages + other.pages)


b1 = Book("ramayana", 2000)
b2 = Book("mahabaratha", 2000)
b1 + b2


# Abstraction

class Myclass(ABC):

    @abstractmethod
    def clauculate(self):
        pass


class Squre(Myclass):
    def clauculate(self, x):
        print()
        print(" squre of number is : ", x * x)


s1 = Squre()
s1.clauculate(10)


