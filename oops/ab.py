from abc import ABC,abstractmethod
import math
class Myclass(ABC):
    @abstractmethod
    def caluculated(self,x):
        pass

class Sub1(Myclass):
    def caluculated(self,x):
        print("squre value =", x * x)

class Sub2(Myclass):
    def caluculated(self,x):
        print("squre root of",x,"is",math.sqrt(x))


class Sub3(Myclass):
    def caluculated(self,x):
        print("cube value of ",x , "is",x ** 3)


obj1 = Sub1()
obj1.caluculated(2)
obj2 = Sub2()
obj2.caluculated(9)
obj3 = Sub3()
obj3.caluculated(2)