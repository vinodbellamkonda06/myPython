import re
with open(r"C:\Users\Jagadeesh\Desktop\books.txt") as f:

    k = f.readlines()
    print(k)

    del k[0],k[1],k[-1],k[-2]
    print(k)
    with open(r"C:\Users\Jagadeesh\Desktop\books1.txt","r+") as f1:
        f1.writelines(k)

        


#    print(data)
#    k = re.findall(r"bk[0-9]+",data)
#    j = re.findall(r"[0-9]+-[0-9]+-[0-9]+",data)
#    l  = re.findall(r"[<w+>[0-9]+.[0-9]+<w+>",data)
