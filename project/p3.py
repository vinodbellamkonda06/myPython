fac_list = []

def factors(num):
    count = 1
    for i in range(1, num + 1):
        if num % i == 0:
            fac_list.append(i)
            count *= i
            if count == num:
                break

factors(600851475143)
print(fac_list)


