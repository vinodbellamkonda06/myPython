import time
# import pdb;pdb.set_trace()
def time_cl(function):
    def count():
        t1 = time.time()
        l = function()

        time.sleep(1)

        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)) + "\n")
        print(l.__next__())
        print(l.__next__())

    return count

#@time_cl
def my_gen():
    return "python"
    return "java"
    # yield "123"
    # yield "qwee"
print(my_gen())
print(my_gen())
print(my_gen())
print(my_gen())
#print(a)
#print(a.__next__())


