'''class Employee:
    id = 0
    num_of_employees = 0
    raise_amount = 1.4

    def __init__(self, f_name, l_name,pay=None):
#        self.id +=1
        self.f_name = f_name
        self.l_name = l_name
        self.pay = pay
        self.email = f_name + "." + l_name + "@company.com"
        Employee.num_of_employees += 1

    def display(self):
        self.id = +1
        print("id:",self.id,"\n",
              "name:", "{} {}".format(self.f_name,self.l_name), "\n",
              "pay:", self.pay, "\n",
              "Email_id:", self.email)

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)
class Student(Employee):

    def marks(self):
        print("name:", self.f_name)




std1 = Student("madhu","sudhan")
emp1 = Employee("bellamkonda","vinod",2000)
emp2 = Employee("manoj","kumar",20000)
Employee.set_raise_amount(2.0)
k = "bk-sanjeev-10000000"
emp3_str = Employee.from_string(k)

print(emp3_str.display())
print(emp2.display())
print(emp1.display())
#print(emp1.__pay)

print(emp1.pay)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.__dict__)
print(Employee.__dict__)
Employee.raise_amount = 1.5
print(Employee.raise_amount)
print(emp1.raise_amount)
print(Employee.num_of_employees)
'''
'''
class parent:
    y=10
    def __init__(self):
        self.y=2
    def add(self,a,b):
        #parent.y=0
        print(a+b)
    def mul(self,a):
        print(a*parent.y)
parent().add(10,20)
parent().mul(20)"""


s='praveen kumar'
x=''
for i in s:
    x=i+x
print(x)

l=[10,20]
m=[10,20]
#m=l
print(l == m)
print(l is m)
print(id(m),id(l))
class My:
    def __init__(self):
        self.__y = 3
m = My()
print(m._My__y)'''


class A:
    def addition(self,a,b):
        print(a + b)

obj = A()
obj.addition(20,10)

class B:
    def multiplication(self,*args):
        #print(args)
        for i in args:
            i =i
            print(i)

obj = B()
obj.multiplication(1,2,3)
