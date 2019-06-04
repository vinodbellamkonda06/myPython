import re
f = open(r'C:\Users\Jagadeesh\Desktop\sample.txt')

data = f.read()
f.close()
# data1 = f.readline()
# data2 = f.readlines()
d = re.findall(r'\w+', data)

print(d)

for word in d:
          ##print((word))
          ##word.upper()
          ##print(word)
          f1 = open(r"C:\Users\Jagadeesh\Desktop\sample2.txt", 'a')
          f1.writelines(word.upper())
          f1.close()
