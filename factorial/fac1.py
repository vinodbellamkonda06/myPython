num = int(input("enter number:"))
def factorial(num):
   if num == 1 or num == 0:
       return 1
   elif num < 0:
       print("enter valid number")
   else:
       return num * factorial(num - 1)
print("the factorial of  ",num,"is",factorial(num))
