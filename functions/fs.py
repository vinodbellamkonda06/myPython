#a = int(input("enter a number:"))

'''odd_list = []
even_list = []

def odd_even_chech():
    for i in range(1,a):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

odd_even_chech()
#print(even_list)
#print(odd_list)'''


n = int(input("enter a number:"))
for j in range(2, n):
    if n % j == 0:
        print("not a prime number:")
        break
else:
    print("prime:")




