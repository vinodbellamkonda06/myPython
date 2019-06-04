"""
Abstraction:
    The process hiding the unnecessary information to the user and providing only required information is known as abstraction.
    >>Abstraction is method to hide internal functionalities from the user.
**Abstract method:
        >>a method whose action\requirement are redefined in the sub classes.
        >>abstract method is method written without body,the body will be redefined in the sub class.
        >>it is possible to write absract method with body also
        >>To mark a method as abstract method write a @abstractmethod decorator on the top of it.
**Abstract class:
        >>Abstract class is class contains some abstract methods.
        >>once abstract class is declare we have to create sub class for if for implementing the methods in it.

"""


from abc import ABC, abstractmethod


class Myclass(ABC):
    @abstractmethod
    def caluculate(self,  x):
        pass


class Squre(Myclass):
    def caluculate(self, x):
        print("squre of given number is:", x * x)


class Cube(Myclass):
    @classmethod
    def caluculate(cls, x):
        print("cube of given number is:", x * x * x)


#s1 = Squre()
#s1.caluculate(2)
#c1 = Cube()
#c1.caluculate(3)
Cube.caluculate(3)


class Car(ABC):
    def __init__(self, regno):
        self.regno = regno

    def open_tank(self):
        print("fill the fuel into the tank:")

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def breaks(self):
        pass


class maruthi(Car):
    def steering(self):
        print("maruthi uses manual sreering:")

    def breaks(self):
        print("maruthi uses hydralic breaks:")

m1 = maruthi("Ap-03-4545")
print(m1.regno)
m1.open_tank()
m1.steering()
m1.breaks()


'''
Interfaces:
    >>Abstract class is a class which contains some abstract&concrete methods.
    >>class which contains only abstract methods then it will become an interface.
    >>an abstract class is called interface.
'''
