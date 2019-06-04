class Student:
    x = 10
    def display(self):
        pass
    @classmethod
    def modify(cls):
        pass
    @staticmethod
    def method():
        pass

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

    def display(self):
        print("oyy")


class C(B, A):
    '''def __init__(self):
        self.c = "c"
        print(self.c)
        super().__init__()'''
    def display(self):
        print("hii")
        super().display()


c = C()
c.display()


class M:

    def add(self, a, b):
        print(a +  b)

    def add(self, a, b, c):
        print(a + b + c)


m = M()
m.add(1,2,7)


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        print(self.pages + other.pages)


b = Book(100)

class Book1:
    def __init__(self, pages):
        self.pages = pages

b1 = Book1(200)

print(b + b1)

