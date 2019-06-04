print("largest palindrome number multiple of two 3 digit prime numbers")
pal=[]
for num in range(900,1000):
    for num1 in range(900,1000):
        k=num*num1
        if k>10:
            kstring=str(k)
            if (kstring==kstring[::-1]):
                h = num * num1
                pal.append(h)
print(pal)
print(max(list(set(pal))))
#u=sorted(list(set(pal)))
#print(u[-1])