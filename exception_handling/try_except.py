s="aaabbbcccdeaa"
cnt=0
val=[]
for i,j in enumerate(s):
    try:
        if s[i] == s[i+1]:
            cnt+=1
        else:
            cnt+=1
            val.append(j,str(cnt))
            cnt=0
    except:
        cnt+=1
        val.append([j,str(cnt)])

print(val)