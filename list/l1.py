l = [1, 2, 1, 2, 3, 4]
k = []

for i in l:
    if i not in k:
        k.append(i)
print(k)
D = ["go", "bat", "me", "eat", "goal", "boy", "run", "pnl"]
arr = ["a", "e", "i", "o", "u"]
l= set()
for i in D:
    k=list(i)
    for j in k:
        if j in arr:
            l.add("".join(i))
print(l)

def fun():
   print("hello")

a = fun()
print(a)