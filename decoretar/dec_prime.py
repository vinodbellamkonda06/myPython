'''import time
def time_cal(function):
    def time_count():
        t1 = time.time()
        w = function()
        time.sleep(1)
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)) + "\n")
        return w
    return time_count

n = int(input("enter a number"))
@time_cal
def prime_num():
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
a = prime_num()
#print(a.__next__())
#print(list(a))
for i in a:
    print(i,end=",")'''

import time
def time_count(function):
    def count(a):
        t1 = time.time()
        function(a)
        time.sleep(5)
        t2 = time.time()
        print("time caluculation:" ,((t2 - t1)) , "\n")
    return count


@time_count
def my_fun(n):
    if n > 1:
        if n <=2:
            print('not a prime:')
        else:
            for i in range(2,n):
                if n % i ==0:
                    print("no")
                    break
            else:
                print("s")



w = my_fun(10)


