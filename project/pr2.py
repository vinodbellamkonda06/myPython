l = [1, 2]
[l.append(l[-1]+l[-2]) for i in range(10) if len(l) < 10]
print(l)