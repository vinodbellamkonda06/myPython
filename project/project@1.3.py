prime = 1
number = 1
while number != 10002:
    prime += 1
    for x in range(2, prime):
        if prime % x == 0:
            break
    else:
        number += 1
print(prime)
