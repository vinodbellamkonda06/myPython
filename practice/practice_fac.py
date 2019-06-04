num = int(input("enter a number for factorial caluculation:"))
def fac(num):
        if num == 1 :
            return 1
        else:
            return num * fac(num  - 1)
if num < 0:
        print("for Negative numbers factorial is not possible:")
elif num == 0:
    print("factorial of",num,"is",1)
else:
    print("the factorial of ",num,"is",fac(num))
