def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return (fibonacci(n-1))+(fibonacci(n-2))
#n = int(input("Enter number of terms:"))
for i in range(10):
    print(fibonacci(i))
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
#n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(5):
    print (fibonacci(i))