class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name :',self.name)
        print('age :',self.age)


class Men(Person):
    pass

m1 = Men("vinod", 23)
m1.display()

class Women(Person):
    def hobbies(self):
        pass

w1 = Women("xzx",23)
w1.display()

class A:
    pass
class B(A):
    pass
class C(B):
    pass
c = C()