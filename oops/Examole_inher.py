'''
Inheritence:
            The process of creating a new class from existing class is known as Inheritence
            parent class-child class
            base class - sub class
            super class -derived class
Types if inheritence:
    1.single level inheritence.
    2.multilevel inheritence.
    3.multiple inheritence.

1.single level inheritence:
        creating one or more class by using single parent class is known as single level inheritence
in this case we have only one base class but we have n number of sub class are derived from it
Example:
    consider Bank is main class from this we can cerate Andra bank,state bank,canara bank
    these all banks are derived form the base class class i.e here base class is only but we have so many sub classes
    this is called single level inheritence
2.multi level inheritence:
         The process creating new class from the previous class is known as multi level inheritence

3.multiple inheritence:
        cerating new class by using one are more class is known is multiple inheritence

*** To know the how the control flow in multi level inheritence use classname.mro() it wiil return
        list of control flow
*** super class  constructor also avaliable to the base class by default like all the members


'''

#This is the example for single level inheritence
class Teacher:
    #this is the base\super\parent class for Student
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Student(Teacher):
    #this is the sub\derived\child class for Teacher
    def set_marks(self,marks):
        self.marks = marks

    def get_marks(self):
        return self.marks


s1 = Student()
s1.set_id(1)
s1.get_id()
s1.set_name("vinod")
s1.get_name()
s1.set_marks(916)
s1.get_marks()
# super class constructor is also avaliable in derived class


class Father:

    def __init__(self):
        self.property = 80000000000.00

    def display_property(self):
        print("fathers property is:", self.property)


class Son(Father):
    pass


s = Son()
s.display_property()
"""
Method overriding:
    >>If you write a constructor in sub class,the super class constructor is not avaliable
    to the sub class.
    >>so super class constructor is not accessible by sub class object.This means sub class 
    constructor is replacing the super class constructor this is called **constructor overriding**
    >>similarly if we write a method inside a sub class with exactly same name in the super class
    it will over ride the super class method this is called **method overriding**
    
"""

#program is example for consructor overriding


class Father:

    def __init__(self):
        self.property = 80000000000.00

    def display_property(self):
        print("fathers property is:", self.property)


class Son(Father):
    def __init__(self):
        #super.__init__()
        self.property = 9000000.00


    def display_property(self):
        print("son's property is:", self.property)


s = Son()
s.display_property()

"""
Super()Method:
    >>super() is builtin method which is usefull to call the super class constructor or methods from the derived class.
    >>Any constructor written in the super class is not avaliable to the sub class if sub class has constructor.
    >>So we need to initilize the supe class constructor in derived class  by using super() method in side the serived class constructor.
    >>super() is method which contains the history of the super class methods.
    >>syntax for use super() method
        ** super().__init__() for calling super class constructor 
        **super().__init__(arguments) calling super class constructor with arguments
        **super().method() for calling super class methods
    >>
"""


class Father:

    def __init__(self, property = 0):
        self.property = property

    def display_property(self):
        print("fathers property is:", self.property)


class Son(Father):
    def __init__(self, property1=0, property = 0):
        #super.__init__(property)
        self.property1 = property1


    def display_property(self):
        print("son's property is:", self.property1)


s = Son(200000,8000000)
s.display_property()

#multiple inheritence


class A:
    def __init__(self):
        self.a = "a"
        print(self.a)
        super().__init__()


class B:
    def __init__(self):
        self.b = "b"
        print(self.b)
        super().__init__()


class C(A,B):
    def __init__(self):
        self.c = "c"
        print(self.c)
        super().__init__()


c = C()
#to know how flow goes in multiple inheritence use classname.mro()
print(C.mro())

