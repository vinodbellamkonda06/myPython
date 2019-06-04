def fact(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n -= 1
    return factorial
for i in range(1,11):
    print("Factorial of {} is {}".format(i,fact(i)))


def prime(n):
    while n% 2 != 0 or n == 2:
        print("given ",n, "is prime:")
        break

        #n -= 1
for i in range(2,10):
    prime(i)
#prime(range(10))