#print(l)
l = [1,3,5,7]
k = []
for i in range(max(l)):
    if i in l:
        pass
    else:
        k.append(i)
#print(k)
#print(l)


#print(m)
#print(z)
#g = {k:v for k,v in m }
#print(g)
#print(d.items())
#print(2<<4)
#print(2>>4)

import collections
#p = collections.OrderedDict(d.items())
#print(p)

'''n = int(input("enter a number:"))
j = 1
if n >= 0:
    if n == 1 or n == 0:
        print("1")
    else:
        for i in range(1,n+1):
            j = j * i
        print(j)
else:
    print("not valid:")'''

#input_set = {1, 2, 3, 4, 5}

for item in range(5):
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
    print ("Factorial of", item, "is", fact)
def factorial(num):
    f = 1
    if num >= 0:
        if num == 0 or num == 1:
            return 1
        else:
            for i in range(1,num+1):
                f = f * i
    print(f)
factorial(3)

def fac_num():
    pass

l = [2, 7, 33, 1, 9]

def b_sort(l):
    c = len(l)
    for i in range(c):
        for j in range(0, c-i-1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l [j]
b_sort(l)
print(min(l))

o_l = set()
e_l = set()
for i in range(10):
    if i % 2 != 0:
        o_l.add(i)
    else:
        e_l.add(i)
print(o_l)
print(e_l)
l.sort()
print(l[-2])