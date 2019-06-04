import re

with open(r"C:\Users\Jagadeesh\Desktop\detail.txt", "r") as fr:
    data = fr.read()
    data1 = re.findall(r"\w+", data)
    data2 = re.findall(r"\d{10}", data)
    print(data2)
    list_word = {}
    i = 1
    for word in data1:
        if word not in list_word:
            list_word[word] = i
        else:
            i = list_word[word]
            list_word[word] = i + 1
print(list_word.items())
print(list_word)
