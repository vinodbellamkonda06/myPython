'''def fun1(a):
    print(a)

def fun2():
    print(a)
fun2()
fun1(10)'''


def fun1(a):
    def fun2():
        print(a)
    fun2()


fun1(10)

list1 = [1, 2, 3, 4, 5, 6]

# function to check weather the number exists in list or not


def search_num(num):

    if num in list1:
        print("The numbr exists:")
    else:
        print("number not exist:")


num = int(input("enter a number to search in list:"))
search_num(num)
