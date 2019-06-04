class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class B:
    def __init__(self, section, number):
       super().__init__(self.name,self.age)
       self.section = section
       self.number = number

    def display(self):
        A.display(self)
        print(self.section)
        print(self.number)

b = B()
b.display()