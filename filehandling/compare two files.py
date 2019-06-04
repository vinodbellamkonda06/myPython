f1=open(r"C:\Users\Jagadeesh\Desktop\data.txt","r")
f2=open(r"C:\Users\Jagadeesh\Desktop\data2.txt","r")
f3=open(r"C:\Users\Jagadeesh\Desktop\data3.txt","w")
def com_file():
    for line in f1:
        for line1 in f2:
            if line == line1:
                f3.write("%s\n" % (line))
            else:
                return com_file()




