#class can be defined as blue print\instance factory for creating objects
'''in oops concept we have two types of variables are there they are
    1.instance variables:
        instance variables are variables whose separate copy is avaliable to all the instances\objects
    2.class variables:
        class variables are the variables whose single copy is available to the
            all the instances of class
'''


class sample:
    """example for class variable"""
    x = 10

    @classmethod
    def modify(cls):
        cls.x += 1


s1 = sample()
s2 = sample()
print(s1.x)
print(s2.x)
s1.modify()
'''if you modify the class variable for one instance it will also effect to the remaning also'''
print(s1.x)
print(s2.x)

class sample:
    '''example for instance variables'''

    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1


s1 = sample()
s2 = sample()
#print(s1.x)
#print(s2.x)
s2.modify()

#if you modify the instance variable for instance it effect for only for that
    #particular instance it will not effect the remaning instances

#print(s1.x)
#print(s2.x)


'''
different types of methods 
    1.instance method
        a.accessor methods(getters)
        b.mutator methods(setters)
    2.class methods
    3.static methods
1.instance methods:
        This methods are act on instance variables of the class are called instance methods
        These methods are bounded to instances\objects(instancename.method)
        Which having first parameter is self(it contains the addres\memory location of the object)
    a.ACCESSOR METHODS:
        These methods simply read\acces the data from the variables
        They do not modify the data in the variables
        These methods written in the form of get<any name>()
        These also called as getters
    b.MUTATOR METHODS:
        These methods will modify the exisisting data in the variables
        These method are written in the form of set<any name>()
        These methods are also called as setters
2.class methods:
    The methods which act on the class variables are called class methods 
    Which have the first parameter is cls(which refers class it self)
    These can be declared by decorator @classmethod at the of the method
    
3.static methods:
    These methods are normal functions which does't have any first parameter like class\instance methods
    These will not act on class\object variables
    These methods can be declared by @staticmethod at the top of method
    These are used for counting the objects or changing the other class variables 
    These methods called by using classname.method()''
#this progarm is example for explaning about instance methods
class student:

    def __init__(self, n = "", m = 0):
        self.name = n
        self.marks = m

    #This is instance method
    def display(self):
        print("hii", self.name)
        print('your marks is', self.marks)


s1 = student("vinod", 30)
s2 = student("kumar", 40)

#this program is example for explaning about getters\setters
#if your going to use setters\getters methods no need to use __init__(self) method

class Employee:

    #setter method
    def setname(self, name):
        self.name = name
    #getter method
    def getname(self):
        return self.name
    def setage(self,age)
        self.age = age
    def getage(self)
        return self.age


e1 = Employee()
e1.setname("vinod")
print(e1.getname())
e2 = Employee()
e2.setname("sreenu")
print(e2.getname())

# this program is example for explaning class methods

class Person:
    eyes = 2

    #this is class method
    @classmethod
    def look(cls, name):
        print("{} looks with {} eyes".format(name,cls.eyes))


Person.look("vinod")
Person.look("kumar")'''

#this program is example for explaning staticmethods

class Oyy:
    n = 0

    def __init__(self):
        Oyy.n = Oyy.n + 1
    def __delete__(self,):
        print("deleted")

    @staticmethod
    def no_of_objects():
        print("noumber of instances created:",Oyy.n)
obj1 = Oyy()
obj2 = Oyy()
print(Oyy.no_of_objects())
del obj2
print(Oyy.no_of_objects())


#passing one class members to another class

'''class Labour:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("id", self.id)
        print("name:", self.name)
        print("salary:", self.salary)
#this class display employee details

class Myclass:
    #method to recive Employee class instances
    #and display the employee details
    @staticmethod
    def mymethod(obj1):
        obj1.salary += 10000
        obj1.display()


obj1 = Labour(1, "vinod", 30000)
Myclass.mymethod(obj1)

#inner class

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print("name:", self.name)

    class Dob:
        def __init__(self, dd, mm, yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy
        def display(self):
            print("dob = {}/{}/{}".format(self.dd, self.mm, self.yy))


p = Person(1, "vinod", 23)
p.display()
x = p.Dob(19, "March  ",1995)
x.display()"""
