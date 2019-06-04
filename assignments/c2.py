import datetime
import time
timestamps = ['2011-06-2', '2011-08-05', '2011-02-04', '2010-1-14', '2010-12-13', '2010-1-12', '2010-2-11', '2010-2-07', '2010-12-02', '2011-11-30', '2010-11-26', '2010-11-23', '2010-11-22', '2010-11-16']
#k = []

'''for i in l:

    m =(list((i.split('-'))))

    k.append(tuple(map(lambda x:int(x),m)))

print(k)'''

'''for i in  range(len(k)):
    if k[i][2] == k[i + 1][2] == k[i + 2][2]:
        if k[i][1] == k[i + 1][1] == k[i + 2][2]:
            if k[i][1] == k[i + 1] == k[i + 2][2]:
                print(k)
            elif k[i][1] == k[i+1][1] or k[i][1] == k[i + 2][1]:
                pass'''


#print(sorted(l, key=lambda d: map(int, d.split('-'))))

#dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in l]

#print(dates.sort())
#sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
#print(sorteddates)

l = timestamps.sort(key=lambda x: time.mktime(time.strptime(x,"%Y-%m-%d")))
print(l)
