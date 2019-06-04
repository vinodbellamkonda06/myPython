"""n = int(input("Enter a number:"))
l = 0
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        l += i
print(l)"""

"""n = int(input("enter a number:"))
f = 1
sum = 0
for i in range(1,n+1):
    f = f * i
for j in str(f):
    sum += int(j)
print(sum)

print(lambda x, y: x + y, [int(i) for i in str(2 ** 1000)])"""

def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    a = (num % 2)
    print(a,end="")

# decimal number
number = int(input("Enter any decimal number: "))

decimalToBinary(number)

print(bin(10))



