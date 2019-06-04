import operator
import pdb;pdb.set_trace()
#print("arrange dictionary values in ascinding and descending order")

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ', d)
sorted_d = sorted(d.items(), key = operator.itemgetter(0))
print('Dictionary in ascending order by value : ', sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
print('Dictionary in descending order by value : ', sorted_d)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print("program to concatanate dictionary")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print(" Python script to check if a given key already exists in a dictionary.")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d={"name":"vinod","place":"rmd","age":22}


def is_key_present(x):
    print(d)
    # x=int(input("enter a key"))
    if x in d:
        print("key exisist in dictionary")
    else:
        print("key not exisist in dictionary")
is_key_present(1)


print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print(" Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)")
d = {x: x*x for x in range(10)}
print(d)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print(" Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys")
d = {x: x*x for x in range(1, 16)}
print(d)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print(" Python program to sum all the items in a dictionary.")
d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
print(sum(d.values()))
print((d.values()))
cnt = 0
mul = 1
for i, j in d.items():
    cnt += j
    mul = mul*j
print(cnt)
print(mul)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print("convert two list into a dictionary")
l=[1, 2, 3, 4]
m=["vinod", "kumar", "hello", "hii"]
d = {}
k = zip(l, m)
for i, j in k:
    d[i] = j
print(d)
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
print("Python program to get max and minimum values from dictionary values")
d1 = {'a': 100, 'b': 200, 'c': 300}
l = []
for i, j in d1.items():
    l.append(j)
print(l)
print(max(l))
print(min(l))
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
my_dict = {'x': 500, 'y': 5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])
print("----- ------ ------- ------- ------ ------ ------ ------ ------ ----- ------")
dict1 = {"a": 10, "b": 20, "c": 30, "A": 40, "B": 50}
dict2 = {}
for i in dict1:
    dict2[i.lower()] = dict1.get(i.lower(),0) + dict1.get(i.upper(),0)
print(dict2)
d = {"a": 10, "b": 20, "c": 10, "d": 20, "k": 40}
s = {}
for i, j in d.items():
    if j not in s:
        s[j] = []
    s[j].append(i)
print(s)
