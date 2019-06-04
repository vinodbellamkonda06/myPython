'''class A:
    def __init__(self, name, age, place, accno, balance):

        self.accno = accno
        self.balance = balance
        self.name = name
        self.age = age
        self.place = place
    def display (self) :

        print( " name :",self.name, "\n" ,
             "age :", self.age, "\n" ,
              "place:", self.place, "\n" ,
              "account number:", self.accno, "\n" ,
              "balance:", self.balance, "\n" )
    def deposit(self, amount):

        self.balance = self.balance + amount

    def withdraw(self, amount):

        if amount <= 500:
            print("maintain minimum balance:")
        elif amount >= self.balance:
            print("insuffient funds")
        else:
            self.balance = self.balance - amount
class Employee(A):


    def employe_details(self, salary):
        self.salary = salary
        print(self.salary)


class Custmer(A):
    def custmer_details(self):
        pass
obj = Employee("vinod", 22, "ramadurgam", 12406, 500)
obj.employe_details(10000)
obj.display()
obj1 = Custmer("kumar", 22, "bang", 12405, 10000)
obj1.display()
obj.withdraw(1000)
obj.display()'''


class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print("id:", self.id, "\n", "name:", self.name, "\n", "age:", self.age,)

#t1 = Teacher(1, "vinod", 22)
#t1.display()


class Teacher(Student):

    def __init__(self, id, name, age, salary):
        super().__init__(id , name, age)
        self.salary = salary

    def display(self):
        super().display()
        print("salary:", self.salary)


t1 = Teacher(1, "vinod", 22, 2222222)
t1.display()
