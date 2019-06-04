# from collections import Counter
# from collections import OrderedDict
# from collections import defaultdict
# from collections import deque
#
#
#
# word = "google"
# count = Counter(word)
# print(count)
#
# players = {"sachin": "cricket", "vinod": "cricket", "sreenu": "football", "venu": "runner", "manju": "khokho" }
#
# sports = defaultdict(list)
#
# for i, j in players.items():
#     sports[j].append(i)
#
# print(sports)
#
# sports1 = {}
#
# for k, v in players.items():
#     if v not in sports1:
#         sports1[v] = [k]
#     else:
#         sports1[v].append(k)
#
# print(sports1)
#
# num_list = deque([1, 2, 3])
# num_list.appendleft(5)
# print(num_list)
# print(dir(num_list))
#
# d = {"name": "vinod", "age": 23, "location": "bangalore"}
# employe_dic = OrderedDict()
# employe_dic[1] = 1
# employe_dic[18] = 17
# employe_dic[13] = 4
#
# print(employe_dic)
# print(d)
#
#
# num = deque([])
# num1 = []
# print(dir(num))
# print(dir((num1)))

players1 = {"sachin": "cricket", "vinod": "cricket", "sreenu": "football", "venu": "runner", "manju": "khokho" }

s = {}

for i, j in players1.items():
    if j not in s.keys():
        s[j] = [i]
    else:
         s[j].append(i)

print(s)

