#a=[1,2,3]
#b=["one","two","three"]
"""a = ["act", "tea", "node", "ate", "cat", "done", "tab", "eat", "xyz", "bat"]
from collections import defaultdict
d=defaultdict(list)
for i in a:
    b="".join(sorted(i))
    d[b].append(i)
print(d.values())

a=[1,2,3]
b=["one","two","three"]
l=[]
for i in enumerate (a):
    for j in enumerate(b):
        if i[0]==j[0]:
            l.append((i[1],j[1]))
print(l)"""
a = ["act", "tea", "node", "ate", "cat", "done", "tab", "eat", "xyz", "bat"]
d={}
for i in a:
    b="".join(sorted(i))
    if b not in d:
        d[b]=[]
    d[b].append(i)
print(d.values())
