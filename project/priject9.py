l = []
for i in range(2,1000):
    print(i)
    for j in range(2,i):
        #print(i,j)
        if i % j ==0:
            continue
    else:
        print(i,"o")
        l.append(i)
print(l)
