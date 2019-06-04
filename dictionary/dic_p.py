from collections import OrderedDict
from collections import deque
from collections import defaultdict
from collections import Counter

d = {1: 2, 3: 4, 4: 1}
a = sorted(d.items(), key=lambda x: x[1])
print(a)
dic = {1: "apple", 2: "mango", 3: "banana", 4: "orange"}
print(dic.items())
print(sorted(dic.items(), key=lambda x: x[1]))
s = {k: v for v, k in dic.items()}
print(s)
dict1 = {"a": 10, "b": 20, "c": 30, "A": 40, "B": 50}
dic2 = {}
for key in dict1:
    dic2[key.upper()] = dict1.get(key.lower(), 0) + dict1.get(key.upper(), 0)
print(dic2)

d = OrderedDict()
d[1] = "vinod"
d[2] = "kumar"
d[3] = "406"
print(d)

number_list = deque()
number_list.appendleft("vinod")
number_list.extend([1, 2, 3, 4, 5])
print(number_list)

w = defaultdict(set)

a = ["act", "tea", "node", "ate", "cat", "done", "tab", "eat", "xyz", "bat"]

for word in a:
    i = "".join(sorted(word))
    w[i].add(word)
print(w)


c = Counter("google")
print(c)

string = "google"
counter_dict = {}

for i in string:
    if i not in counter_dict:
        counter_dict[i] = 1
    else:
        k = counter_dict[i]
        counter_dict[i] = k + 1
print(counter_dict)

c = defaultdict(int)

for i in "google":
    c[i] += 1
print(c)