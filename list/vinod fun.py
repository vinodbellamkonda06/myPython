list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
list3 = []

k=zip(list1,list2)
l=sorted(k,key=lambda k:k[1])
print(l)
for i,j in l:
    list3.append(i)
print(list3)
#from geeksforgeeks
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]



a = 10
b = []
def fun(a):
    b.append(a)
    print(b)

fun(a)
a = [1,2,3]
fun(a)
fun((1,2))
