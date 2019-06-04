def isprime(a):

    if not a%2:
        return False

    for i in range(3,a,2):
        if a%i == 0:
            return False
    return True


def nth_prime(n):
    prime_numbers = []
    i = 2
    while len(prime_numbers) < n:
        if isprime(i):
            prime_numbers.append(i)
        i += 1
    print(i-1)


nth_prime(10001)
