l = [1,[1],[1,2,[1,2]]]
m = []
k = []
for i in l:
    try:
        if type(i) == list:
            k.extend(i)

    except TypeError as e:
        pass
    finally:
        pass
        '''for i in k:
            if type(i) == int:
                k.append(i)
            else:
                k.extend(i)'''


print(k)
l = [i for i in range(10) for j in range(2,i) if i % j == 0]


