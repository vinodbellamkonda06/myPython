'''val1=int(input("enter a value:\n"))
list1=[0,1]
for i in range(1,val1):
    list1.append(list1[-1]+list1[-2])
print (list1)
print(3 == 4 - 1)'''




'''import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        print("make sure password contains between 6 to 12 characters")
        break
    elif not re.search("[a-z]",p):
        print("make sure password contains one lowercase")
        break
    elif not re.search("[0-9]",p):
        print("make sure password contains one digit")
        break
    elif not re.search("[A-Z]",p):
        print("make sure password contains One Uppercase")
        break
    elif not re.search("[$#@]",p):
        print("make sure password contains one special symbol")
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")'''


'''l = []
k = []
n = 0
while n < 5:
    i = int(input("enter a number to append list:"))
    l.append(i)
    n += 1
for i in range(len(l)):
    print(i)
    if l[i] == (l[i+1]) +1 :
        k.extend((l[i],l[i + 1]))
    else:
        pass
print(k)'''

l = [100, 1, 200, 2, 3, 101]
l.sort()
print(l)
k = []
try:
    for i in range(len(l)):

        if l[i] + 1 == (l[i + 1]):

            k.extend((l[i], l[i + 1]))
except:
    pass
finally:
    print(list(set(k)))

string = input("enter a string:")

print(" ".join([(i.lower()[::-1]).capitalize() for i in string.split() ]))





