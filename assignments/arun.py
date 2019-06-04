s = "12234 55vin oDKU ree eww"

d_count = 0
u_count = 0
l_count = 0
space = 0

for i in s:
    if i.isdigit():
        d_count += 1
    elif i.isupper():
        u_count += 1
    elif i.isspace():
        space += 1
    else:
        l_count += 1
print(d_count,l_count,u_count,space)
