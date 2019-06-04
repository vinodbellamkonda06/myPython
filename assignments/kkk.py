for i in range(10):
    print(i, end="")

l = [1,2,3,4,5]

d = enumerate(l)
print(list(d))

for i, j in enumerate(l):
    print(i,j)