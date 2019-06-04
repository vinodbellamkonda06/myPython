list = ['apple', 'orange', 'mango', 'banana']

list1 = sorted(list, key=lambda x:x[1])
print(list1)

print(list.sort(key=lambda x:len(x)))
print(list)