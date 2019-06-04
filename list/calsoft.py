l = [1,123,2,1001,4,3,100,101,102]

''''l.sort()

l1 = []
l2 = []

for i in l:
    for j in l:
        if j == i + 1:
            if j not in l1:
                l1.append([i,j])
                for k in l1:
                    if k not in l2:
                        l2.extend(k)
                    else:
                        pass
            else:
                pass
w = sorted(list(set(l2)))

j = []
o = []

for val in range(len(w)):
    try:
        if w[val + 1] == w[val] + 1:
            j.extend([w[val],w[val + 1]])
        else:
            o.append(w[val + 1])
    except:
        o.append(set(j))
        print(o)'''


'''ll = []
temp = l[0]
ll.append(l[0])
keyval = {}

for x in range(1,len(l)):
    #print (str(x)+ "  :"+str(l[x]))
    if l[x] >= temp :
      ll.append(l[x])
      temp = l[x]
      #print (ll)
    else:
      keyval[len(ll)] = ll
      ll=[]
      temp = l[x]

max_key = max(keyval.keys())
print (keyval[max_key])'''

for i in range(len(l)):
    try:

        if l[i + 1] == l[i] + 1:
            pass
        else:
            print("okk")
    except:
        pass





