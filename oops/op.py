class A:
    o_count = 0

    def __init__(self):
        A.o_count += 1

    def display(self,):
        print("Hi this is vinod kumar:")

    def __delete__(self, instance):
        print("deleted:")
        A.o_count -= 1

    @staticmethod
    def display_object_count():
        print("The noumber of objects are created is:", A.o_count)


obj = A()
obj1 = A()
A.display_object_count()
obj.__delete__(obj)
obj1.display()
A.display_object_count()
obj2 = obj1
obj1.__delete__(obj1)
print(obj2)
