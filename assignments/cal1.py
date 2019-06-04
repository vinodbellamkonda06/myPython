l = ['3-4-1994', '3-5-1993', '3-3-1993']
k = []
for i in l:

    m =(list((i.split('-'))))

    k.append(tuple(map(lambda x:(x),m)))

s_list = sorted(k)
for i in s_list:

    m =(list((i.split('-'))))
k1 = sorted(s_list, key=lambda x:s_list)
print(k1)



