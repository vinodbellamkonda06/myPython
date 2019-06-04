'''class arithematic:
    def __init__(self,func):
        self.func = func

    def __call__(self, a, b):
        print("i am in call method:")
        if a > 0 and b > 0:
            z = self.func(a,b)
            print(z)
        else:
            print("enter valid numbers")
@arithematic
def add(a,b):
    return a + b
add(10,20)
@arithematic
def div(a,b):
    return a / b
div(1,0)'''
class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        def __call__(self, func):
            print("i am in call method")
            print(self.a,self.b)
            def func(a,b):
                print("i am in function")
                c = func(a,b)
                print(c)
            return func
@Add("zxcvv",1234 )
def xyz(a,b):
    return a + b
xyz(10,20)