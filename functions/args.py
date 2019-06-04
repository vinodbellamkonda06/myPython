'''k ="3+++3----------4+++4"
l = sum([int(x) for x in k if x.isdigit()])
print(l)


def fun():
    a = 10
    print(a)
fun()
a = 40
fun()
j  = input("str:")
n = int(input("num:"))
str1=j.replace(j[n],'')
print (str1)

str1=j[:n]
str2=j[n+1:]
print (str1+str2)'''

def add(*args):
    c = 0
    for i in args:
        c += i

    print(c)
add(10,20)
add(2,3,4)
add(1,2,3,4,5)

l = [1,2,3,4]
list1 = list(map(str,l))
print(list1)

def add(a=10,b=2):
    print(a + b)
add()

