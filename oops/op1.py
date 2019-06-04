'''class student:

    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):

        print("name :",self.name)
        print("age :",self.age)
        print("id:",self.id)

s1 = student(1,"cnu",22)
s2 = student(2,"bj",22)

s1.display()
s2.display()


class Employee(student):
    def __init__(self, id, name, age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("name :", self.name)
        print("age :", self.age)
        print("id:", self.id)
        print("salary:", self.salary)


#e1 = Employee(1,"kjk",34)
#e1.display()

class labour(Employee):
    pass

'''


class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("name:", self.name)
        print("age:", self.age)


s1 = student("vinod",22)
s1.display()
s2 = student("chenna",23)
s2.display()