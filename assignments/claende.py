import datetime
l = ['1-3-1995', '2-2-1995', '1-4-1995']
k = []
#sorted(k, key=lambda x: datetime.datetime.strptime(x, '%b %d'))

for i in l:
    #print(i)
    m =(list((i.split('-'))))
    k.append(tuple(map(lambda x:int(x),m)))

#date_list = []
#print("@",len(k))
#n = len(k)
'''for i in range(n):
    t1 = k[i]
    t2 = k[i+1]
    t3 = k[i+2]
    break
#print(t1)
#print(i)
for j in range(len(k)):
    #print(t1[j])
    #print(t2[j])
    #print(t3[j])

    if t1[j] >= t2[j] and t1[j] >= t3[j]:
        pass'''
j = [(1, 3, 2016), (2, 2, 2016), (1, 4, 2016)]
y_list = (sorted(j, key=lambda x:x[2]))
#print(sorted([('adc', 121),('abc', 231),('bcc', 148), ('abc',221)], key=lambda x: x[0][1]))
#print(y_list)
m_list = sorted(y_list, key=lambda x:x[1])
#print(m_list)
day_list = sorted(m_list, key=lambda x:x[0])
#print(j)
#print(day_list)
print(y_list)
u = []
n = len(y_list)
for i in range(n):
    #print(i)
    for j in range(1, n - i - 1):
        #print(j)
        if y_list[i][j] > y_list[i + 1][j]:
            #print(y_list[i],y_list[i + 1])
            y_list[i], y_list[i + 1] = y_list[i + 1], y_list[i]

#print(y_list)














