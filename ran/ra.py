import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("enter any number:"))

ran_num = random.choice(l)
print(num, ran_num)

if num == ran_num:
    print("you win:")
else:
    print("try again:")