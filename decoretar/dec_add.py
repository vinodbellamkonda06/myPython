import pdb as __pdb
def cal(fun):
    print(a,b)
    def cal1(a, b):
        if a > 0 and b > 0:
            return fun(a,b)
        else:
            print("enter pasitive numbers")
    return cal1
    print("arun")
a = int(input("enter number:"))
b = int(input("enter number:"))
__pdb.set_trace()
@cal
def add(a,b):
    print(a + b)
add(a,b)

