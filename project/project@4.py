'''def greetPerson(*name):
  print('Hello', name)

greetPerson('Frodo')
greetPerson("vinod")'''

s = 0
for i in range(2,20000000):

    for j in range(2,i):
        if i % j == 0:
            break
    else:
        s += i
print(s)
