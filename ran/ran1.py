import random
def rand(start,stop,num):
    l=[]
    for i in range(num):
        l.append(random.randint(start,stop))
    return l
print(rand(start=1,stop=10,num=10))
print("-------------------------------------------------------------------------------")
arry = [0,1,1,0,0,1,0,1,0,1]

def segrate(arry):
    res = ([x for x in arry if x == 0] + [x for x in arry if x == 1 ])
    print(res)
segrate(arry)
print("-------------------------------------------------------------------------------")
def sortSecond(val):
    return val[0]
list1 = [(1, 2), (3, 3), (1,1)]
list1.sort(key=sortSecond)
print(list1)
list1.sort(key=sortSecond, reverse=True)
print(list1)
print("-------------------------------------------------------------------------------")
T = tuple("geeks")
a,b,c,d,e = T
b = c = "v"
T = (a,b,c,d,e)
print(T)
print("-------------------------------------------------------------------------------")
L = [2e-04, 'a', False, 87]
T = (6.22, 'boy', True, 554)
for i in range(len(L)):
    if L[i]:
        L[i] = L[i] + T[i]
    else:
        L[i] = L[i] + T[i]
        break
print(L)
print("-------------------------------------------------------------------------------")
T = (2e-04, True, False, 8, 1.001, True)
val = 0
for x in T:
    val += int(x)
print(val)
print("-------------------------------------------------------------------------------")
'''L = [3, 1, 2, 4]
T = ('A', 'b', 'c', 'd')
L.sort()
counter = 0
for x in T:
    L[counter] += int(x)
    counter += 1
    break
print(L)'''
print("-------------------------------------------------------------------------------")
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
ar4 = sorted(ar1 + ar2 + ar3)
d = {}
l=[]
def common_number(ar4):
    count = 0
    for i in ar4:
        if i not in d:
             d[i] = ar4.count(i)
        else:
            count = count+1
    for (key,val) in d.items():
        if val == 3:
             l.append(key)
print(common_number(ar4),l[0:])
print("-------------------------------------------------------------------------------")
# Function to find common elements in three
# sorted arrays
from collections import Counter
def commonElement(ar1, ar2, ar3):
    ar1 = Counter(ar1)
    ar2 = Counter(ar2)
    ar3 = Counter(ar3)
    resultDict = dict(ar1.items() & ar2.items() & ar3.items())
    common = []
    for (key, val) in resultDict.items():
        for i in range(0, val):
            common.append(key)
    print(common)
if __name__ == "__main__":
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    commonElement(ar1, ar2, ar3)

num=int(input('guess a number in between 1 and 10'))
x = random.randint(1,10)
print(x)
if num == x :
    print("sucess")
else:
    print("try again")