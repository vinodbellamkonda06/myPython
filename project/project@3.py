'''l=[x for i in range(2,8) for x in range (i*2,100,i)]
m=[x for x in range(2,100) if x not in l]
k=[x for x in m ]
print(k)
def mul_list():
    tot=1
    for i in k:
        tot*=i
        print(tot,i)

mul_list()'''
num=600851475143
l=[]
def fact():
    for i in range(1,num+1):
        if (num%i==0):
            print(i)
            l.append(i)

fact()
def prime():
    for x in l:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")

                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
prime()




