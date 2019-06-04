
import time
def Time_cal(function):
    def time_wrapper():
        t1 = time.time()
        function()
        time.sleep(1)
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)) + "\n")
    return time_wrapper
@Time_cal
def gen_prime():
    l =[]
    for n in range(1,10):
        if n ==1 or n== 2:
            for i in range(2,n):
                if n % i == 0:
                    pass
            else:
                l.append(n)
                print(l)
gen_prime()









