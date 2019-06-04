import re
s = 'My 2 favourite numbers are 7 and 10'
l=re.findall("[0-9]+",s)
print(l)
n="my name is vinod kumar mail id is vinodbellamkonda06@gmail.com,shareyourego45@gmail.com,asddd.123@gamil.com,dob is 19/30/1995,19/march/1995"
o = re.search("[a-zA-Z]+[0-9].@[a-zA-Z]+.[a-zA_Z]+",n)
#o = re.findall("[a-zA-Z0-9._]+@\w+.\w+",n)
print(o)
k = re.findall("[0-31]",n)
m = re.findall("\d+/\w+/\d+",n)
print(k,m)
print("---------- -------- --------- -------- ----- ---- ---- --------")
s = "abbbkkddjbbbkkabdakdbabbbabbbabbbabb"
print(re.findall("ab{2,}",s))
print("---------- -------- --------- -------- ----- ---- ---- --------")
z = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#print(list(z))
print(" ".join(re.split("[A-Z]",z)[1:]))