import re
f = open(r"C:\Users\Jagadeesh\Desktop\os_module.txt")
data = f.read()
#print(data)
s = re.findall(r"\w+",data)
s1 = re.search(r"\w+",data)
#print(s)
#print(s1)


pattern = "C"

s = "IceCeam"
s1 = "Cake C"
k = re.search(pattern,s1).group()
print(k)


l = lambda a,b="to",c="java",:a+b+c
print(l("welcome",c = "python"))


l1 = [1,2,3,4,5]
l2 = []
for i in l1:
    l2.append(str(i))
print(l2)

l3 = map(lambda x:str(x),l1)
print(list(l3))


l = [1, 2, 3, [1, 2], ["python", "java"]]
l1 = []

for i in l:
    if type(i) != list:
        l1.append(i)
    else:
        l1.extend(i)
print(l1)

l2 = l [::-1]
print(l2)