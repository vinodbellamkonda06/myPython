l = [1,2,[1,2]]
t=[]
def flatten(l):
    for i in l:
        if type(i) !=list:
             t.append(i)
        else:
             flatten(i)


flatten(l)
print(t)
m = []
try:
    for i in l:
        if type(i) == int:
            m.append(i)
except:
    def flatten(l):
        if type(i) == list:
            flatten(i)
        else:
            t.append(i)
    flatten(l)
finally:
    print(t,m)



