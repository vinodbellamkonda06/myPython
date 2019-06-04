num_list = [1, 2, 3, 4, 5]
num_count = len(num_list)
sum_list = sum(num_list)
avg_list = sum_list / num_count
print(avg_list)
count = 0
sum_n = 0
for num in num_list:
    count += 1
    sum_n += num
avg = sum_n / count
print(avg)

print(sum(num_list) / len(num_list))

a = 1
b = 2
c = 3
d = []
d.append(a)
d.append(b)
d.append(c)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if i != j & j != k & k != i:
                print(d[i], d[j], d[k])

n = 4
a = []
#import pdb;pdb.set_trace()
for i in range(1, n + 1):
    print(i, sep=" ", end=" ")
    if (i < n):
        print("+", sep=" ", end=" ")
    a.append(i)
print("=", sum(a))

#print()

n = 3
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()