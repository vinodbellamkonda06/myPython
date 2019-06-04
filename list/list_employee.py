emp = []

n = int(input("enter how many employees you want to insert:"))

for i in range(n):
    print("enyter id: ",end="")
    emp.append(int(input()))
    print("enter name :",end="")
    emp.append(input())
    print("enter salary :",end="")
    emp.append(float(input()))
#print(emp)
id = int(input("enter employee id:"))
for i in range(len(emp)):
    if id == emp[i]:
        print("id = {:d},name = {:s},salary = {:2f}".format(emp[i],emp[i+1],emp[i+2]))
        break

