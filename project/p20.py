num = 100
fac = 1

for i in range(1, 101):
    fac *= i
print(sum([int(x) for x in list(
    str(fac))]))