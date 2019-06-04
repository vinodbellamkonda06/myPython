'''
Regular expression is tool used to extract information from the file\server from anywere.
python provides a module for this that is re.we have to import this.
In re module we have different methods available i.e.. search,findall,match,compile...etc

Regular expression are used perform the following operations:
1.match():by using this method we can match a particular pattern at the begining
2.search():it will search in the entaire data
3.findall():it will gives the all the occurences of the given search pattern
4.split():it will split the data according to the given pattern
5.sub()---> replace:it will replaces the new pattern with old\existing data



'''
import re
with open(r"C:\Users\Jagadeesh\Desktop\detail.txt","r") as f1:
    data = f1.read()
    d1 = re.findall(r"\w", data)
    d2 = re.findall(r"\w+", data)
print(len(d1))
print(len(d2))
print(d1)
print(d2)


s = input("enter a string:")
k = "AEIOUaeiou"
def vowels(s):
    return len(list(filter(lambda letter:  letter in k, s )))
d = vowels(s)
print(d)

def vowel_expression(s):
    return len(letter for letter in s if letter in k)
h = vowels(s)
print(h)