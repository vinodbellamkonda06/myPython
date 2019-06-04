import datetime
'''my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
print(my_dates)'''

l = ['3-4-1994', '3-5-1993', '3-3-1993']
k = []
for i in l:

    m =(list((i.split('-'))))

    k.append(tuple(map(lambda x:int(x),m)))

print(k)
for i in k:
    d = datetime.datetime(1990,2,3)
    print(d)