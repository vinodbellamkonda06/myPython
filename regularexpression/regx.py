import re
data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for i in data:
    #print("".join(re.findall("[^(.com)]", i)))
    print(re.sub(r" ?\([^)]+\)", "", i))

text1 = '**//Python Exercises// - 12. '
d = "".join(re.findall("\w+",text1))
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))
#print(d)
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program to find all words which are at least 4 characters long in a string.")
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r'\b\w{4,}\b',text))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")

text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r'\b\w{5}\b',text))
print(re.findall(r'\b\w{3,5}\b',text))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program that matches a string that has an a followed by zero or more b's.")
import re
def text_match(text):
#    pattern = "ab*"         #for zero or more
#    pattern = "a{3}b"       #for particular number of times {num}
    #pattern = "a?b"         #for zero or one
    #pattern = "a+b"         #for one or more
    #pattern = "a{2,3}b"
    if re.search(pattern, text):

        return "text found"
    else:
        return "text not found:"

print(text_match("abb"))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program to find sequences of lowercase letters joined with a underscore.")
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
import re
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon")
import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))
print(re.sub("[ ,.]", ":", text, 2))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program to separate and print the numbers and their position of a given string")
import re
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program to abbreviate 'Road' as 'Rd.' in a given string")
import re
street = '21 Ramkrishna Road'
print(re.sub('Road$', 'vinod.', street))
print("_____ _______ _______ _______ ________ _________ ___________ __________ _________ __________")
print("Write a Python program that matches a string that has an a followed by zero or more b's.")
x = "aabaaabbbbnnnbaanbbbb"
y = re.search("[ab?]",x)
u = re.findall("ab?",x)
print(u)
print(y)






