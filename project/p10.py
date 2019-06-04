prime_list = 0
for i in range(2, 2000000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_list += i

print(prime_list)
