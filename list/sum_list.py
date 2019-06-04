l = [1,2,3,4,5,1,2,3,9,1,3]
'''def sum_list(l):
    sum = 0
    cnt = 0
    for i in l:
            sum = i + sum
            cnt = cnt+1

        else:
            sum_list(i)
sum_list(l)'''
count = 0
sum = 0
for i in l:
    count = 1 +count
    sum = i+sum
print(count)
print(sum)
list = [1,2,[1,2],(1,2),('mahi')]
m = []

def sum_list(list):
    sum = 0

    for i in list:
        print (i)
        print(m)
        if type(i) == int:
            m.append(i)
            print(m)
        elif type(i) == tuple:
            for n in i:
                m.append(n)
                print (n)

        else:
            m.extend(i)
            print(i)
    print(m)

sum_list(list)

l=[1,2,[3,4],[5,6]]
cnt=[]
def sum():
    for i in l:
        if type(i)==type([]):
            return sum(i)
        else:
            cnt.append(i)
    print(cnt)


def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))