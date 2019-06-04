'''i,a,b = 0,0,1
n = 10
while i<n:
    print(a,end=",")
    a,b = b,a+b
    i += 1'''

'''def fac(n):
    if n < 0:
        return "enter valid number:"
    elif n == 0 or n == 1:
        return "factorial of given",n, "is",1
    else:
         return n * fac(n - 1)
n = int(input("enter a number:"))
print(fac(n))'''
'''num = int(input("enter a number for factorial:"))
fac = 1
if num < 0:
    print("enter a valid number:")
elif num == 1 or num == 0:
    print("factorial of",num,"is",1)
else:
    for i in range(1,num+1):
        fac = fac *i
    print("factorial of",num,"is",fac)'''
def fac(n):
    if n > 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n *fac(n - 1)
    else:
        return "enter a valid number:"



a = fac(3)
print(a)



