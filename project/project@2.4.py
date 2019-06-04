#a=max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])
#print(a)
"""a = 600851475143
l = []
k = 1

for i in range(10000):
    if k != a:
        if i <= 2:
            continue
        elif i % 2 == 0:
            continue
        else:
            if a % i ==0:
                k *= i
                l.append(i)
print(k)
print(l[-1])

n = 2520
for i in range(1, 10):
    if n % i == 0:
        continue
    else:
        print("i am in else:")
else:
    print(n,"is list num divisible by 1 to 10:")"""

import math
# Returns the lcm of first n numbers
def lcm(n):
    ans = 1
    for i in range(1, n + 1):

        ans = (int(ans) * i) / math.gcd(int(ans), i)
        #print(ans)
    return ans


# main
n = 10
print(lcm(n))


