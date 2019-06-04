'''d = {'a': 1, 'c': {'r': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}

for k, v in d.items():
    if type(v) != dict:
        d[k] = v
    else:
        for k1, v1 in v.items():
            if type(v1) != dict:
                d[k1] = v1
            else:
                pass'''



dq = {2:"mango", 1:"grapes", 3:"apple"}

c = dq.items()
print(c)

d = sorted(c, key=lambda x:x[1][0])
print(d)