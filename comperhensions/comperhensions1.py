l = [1,2,3,4,6,8,12]
'''k = [x * x for x in l if x % 2 == 0]
print(k)
z = [[1,2,3],"vinod",(1,2,3),{1:1,2:2},{1,2}]
x = [(i,len(i),type(i)) for i in z if type(i) == list]
print(x)
i = [1,2,3,4]
o = []
d = [o.append(p) for p in i]
print(o,d)
f = [(u,j,u*j)  for u in o for j in i]
print(f)'''
'''d = {i:j for i ,j in enumerate(l)}
print(d)
x = {"a":10,"c":2,"A":2,"m":0}
s = {k.lower():x.get(k.lower(),0) + x.get(k.upper(),0) for k in x}
print(s)'''