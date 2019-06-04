'''n = int(input("Enter a number:"))

if n >= 0:
    fact = 1
    if n == 1 or n == 0:
        print("Factorial of given",n,"is 1")
    else:
        for i in range(1,n + 1):
            fact = fact * i
        print("Factorial of Given ", n, "is", fact)
else:
    print("Enter valid numbers:")
print("______ __________ _________ _________ _________ __________ _________ ___________")

k = int(input("Enter range:"))
for num in range(1,k):
    fac_num = 1
    for j in range(1,num+1):
        fac_num = fac_num * j
    print("Factorial of ",num,"is",fac_num)
print("______ __________ _________ _________ _________ __________ _________ ___________")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print("Enter Valid numbers:")
    else:
        fact = 1
        for i in range(1,num + 1):
            fact = fact * i
        print("Factorial of given ",num,"is",fact)
factorial(4)
print("______ __________ _________ _________ _________ __________ _________ ___________")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print("Enter Valid numbers:")
    else:

        return num * factorial(num - 1)

print(factorial(4))

print("______ __________ _________ _________ _________ __________ _________ ___________")

p = int(input("Enter a number:"))
if p > 1:
    for i in range(2,p):
        if p % i == 0:
            print("Not a Prime Number:")
            break
    else:
        print("Prime number:")
else:
    print("enter more than 1")
print("______ __________ _________ _________ _________ __________ _________ ___________")

q = int(input("ENter Range:"))

for num in range(2,q):
    for i in range(2,num):
        if num % i == 0:
            print("given",num,"Not a Prime Number:")
            break
    else:
        print("given",num,"Prime number:")
print("______ __________ _________ _________ _________ __________ _________ ___________")

def prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("Given",num,"is not a prime number:")
                break
        else:
            print('Given',num, "is prime:")
prime(6)
print("______ __________ _________ _________ _________ __________ _________ ___________")
l = ["kumar","vinod","ball","bat","ok"]
l.sort(key=lambda x :len(x))
d = {1:"vinod",4:"kumar",3:"xzc",2:"asd"}
z = d.items()
m = sorted(d.items(),key=lambda x:x[1])
print("______ __________ _________ _________ _________ __________ _________ ___________")
a = 0
b = 1
i = 0
while(i < 10):
    #print(a,end="")
    c = a + b
    a = b
    b = c
    i += 1
x,y=0,1
l = []
while y<50:
    l.append(y)
    x,y = y,x+y
print([x for x in l if x % 2 ==0])

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(5))


def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n - 1) + fibR(n - 2)


print(fibR(5))

a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("______ __________ _________ _________ _________ __________ _________ ___________")

#num = input("Enter a number:")
num = str(153)
c = 0
if len(num) < 3:
    print("Not a Amstrong number:")
else:
    for i in num:
        c += pow(int(i) , len(num))

if c == int(num):
    print("am")
else:
    print("no")
print("______ __________ _________ _________ _________ __________ _________ ___________")
k = input("enter a number")
l = 0
for i in k:
    l += pow(int(i), len((k)))
else:
    print(l)
    if l == int(k):
        print("am")
    else:
        print("no")'''















