primelist = [2]
num = 3

while len(primelist) != 10001:
    for a in primelist:
        if num % a == 0:
            num += 1
            break
        elif a == primelist[-1]:
            primelist.append(num)
            num += 1
            break
b = primelist[-1]
print("Answer is {}".format(b))