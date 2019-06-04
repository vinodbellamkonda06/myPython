num_list = []
l = 0
for num in range(10000, 100000):
    l = 0

    for i in str(num):
        l += pow(int(i), 5)

        if l == int(num):
            num_list.append(num)
k = 0
m = 0
for i in num_list:
    k = 0

    for j in str(i):


        k += pow(int(j), len(str(i)))


        if k == int(i):

            m += i

print(m - 443839)

s = (i for i in range(10, 1000000) if i == sum(int(d) ** 5 for d in str(i)))
print(list(s))
print(num_list)

