
def CountSquares(a, b):
    cnt = 0 # initialize result

    # Traverse through all numbers
    for i in range(a, b + 1):
        j = 1
        d = 0
        while j * j <= i:
            d += 1
            if j * j == i:
                cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt

print(CountSquares(2,10))


import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))