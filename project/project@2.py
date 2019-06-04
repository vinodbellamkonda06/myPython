print("largest palindrome number multiple of two 3 digit prime numbers")
pal=[]
for num in range(900,1000):
    for num1 in range(900,1000):
        k=num*num1
        if k>10:
            temp = k
            rev = 0
            while (k > 0):
                dig = k % 10
                rev = rev * 10 + dig
                k = k // 10

            if (temp == rev):

                h=num*num1
                pal.append(h)

u=sorted(list(set(pal)))
print(u[-1])
print("@06")

