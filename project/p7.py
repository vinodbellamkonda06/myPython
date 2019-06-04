l = []
for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        if len(l) == 6:
           print(num)
        else:
            l.append(num)


numbers = list(range(2, 2000000))
for prime in numbers:
    for x in numbers:
        if x % prime == 0 and prime != x:
            numbers.remove(x)
print(sum(numbers))
