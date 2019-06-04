prime_list = []
cnt = 0
for num in range(2, 105000):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_list.append(num)
        cnt += 1


print(prime_list[10001])
print(prime_list)
