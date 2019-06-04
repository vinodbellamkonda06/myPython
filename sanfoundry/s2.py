#import pdb;pdb.set_trace()
'''def remove(s, n):

    first = s[:n]

    last = s[n + 1:]
    return first + last


s = input("Enter the sring:")
n = int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(s, n))'''


d = {x:x*x for x in range(1,10)}
print(d)
l = [1,2,3]
k = ["vinod","kumar","manoj"]
d = {x:y for x in l for y in k }
print(d)