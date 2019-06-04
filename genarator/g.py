def gen(num):
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

s = gen(5)
print(s)
print(list(s))
