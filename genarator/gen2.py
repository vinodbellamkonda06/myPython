def pow1():
    for i in range(1, 5):
        yield pow(i, 2)

a = pow1()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


l = iter([1,2,3])
print(l)

