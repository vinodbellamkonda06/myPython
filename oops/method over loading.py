"""class Base(): # Base class
    '''def add(self,a,b):
        s=a+b
        print s'''
    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        sum =a+b+c
        print (sum)
class Derived(Base): # Derived class
    def add(self,a,b): # overriding method
        sum=a+b
        print (sum)
add_fun_1=Base() #instance creation for Base class
add_fun_2=Derived()#instance creation for Derived class

add_fun_1.add(4,2,5) # function with 3 arguments
add_fun_2.add(4,2)   # function with 2 arguments"""


class Arithamatic:
    def addition(self,*args):
        sum = 0
        for i in args:
            sum += i
        print(sum)


obj = Arithamatic()
obj.addition(10,20,30)
obj.addition(10,20)
obj.addition()
