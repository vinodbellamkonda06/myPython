"""l = [1, 2, 3, 4]
print(sum(l)/len(l))

a = 0
z = 0
for i in l:
    a += i
    z += 1
print(a / z)"""


"""n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))"""

"""a, b = 10, 20
print(a, b)
b, a = 10, 20
print(a, b)"""

"""a = int(input("Enter value of first variable: "))
b = int(input("Enter value of second variable: "))
a = a + b
b = a - b
a = a - b
print("a is:", a, " b is:", b)"""

"""n =(input("enter a number:"))
v = n[::-1]
print(int(v))
print(reversed(n))

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)"""

"""n=int(input("Enter number: "))
k = str(n)
k1 = k + k
k2 = k + k + k
print(int(k1) + n + int(k2))"""

"""n = int(input("enter a number:"))
if n ==  0:
    print(" ZERO")
elif n > 0:
    print("positive number:")
else:
    print("negative number:")"""
"""n = int(input("how many subjects marks :"))
a = 0
for i in range(0,n):
    a += int(input("Enter Subject Marks:"))

avg = a / n

if avg > 90:
    print("A grade:")
elif avg > 70:
    print(" B grade:")
elif avg > 60:
    print("C grade:")
elif avg > 50:
    print("D grade:")
elif avg > 40:
    print("E grade:")
else:
    print("F grade:")"""
list = [1,2,5,34,2]
#print(max(list))
list.sort()
print(list[-1])
l = []
m = []
for i in list:
    if i % 2 == 0:
        l.append(i)
    else:
        m.append(i)
print(l,m)
k = [m for m in list if m % 2 == 0]
print(k)
print(sorted(l + m))
v = l + m
v.sort()
print(v)
a=[['A',34],['B',21],['C',26]]
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']

names2 = names1

names3 = names1[:]

names2[0] = 'Alice'

names3[1] = 'Bob'

sum = 0

for ls in (names1, names2, names3):
    print(ls)

    if ls[0] == 'Alice':
        print(ls[0])
        sum += 1

    if ls[1] == 'Bob':
        sum += 10

print(sum)





