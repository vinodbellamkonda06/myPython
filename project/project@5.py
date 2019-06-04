cnt = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 ==0:
        cnt += i
print(cnt)
print("------- ---------- ----------- -------- ---------- ----- ------ ---------- ------ ---- --- ----")
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 ==0 ]))
print("------- ---------- ----------- -------- ---------- ----- ------ ---------- ------ ---- --- ----")
cache = {}
def fiba(n):
     cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fiba(n-1) + fiba(n-2))
     return cache[n]
n = 0
x = 0
while fiba(x) <= 4000000:
       if not fiba(x) % 2: n = n + fiba(x)
       x=x+1
print(n)
print("------- ---------- ----------- -------- ---------- ----- ------ ---------- ------ ---- --- ----")
s = [ x * y for x in range(900,1000) for y in range(900,1000) if str(x * y) == str(x * y)[::-1]]
print(s[-1])
print("------- ---------- ----------- -------- ---------- ----- ------ ---------- ------ ---- --- ----")
cnt = 0
s_cnt = 0
for i in range(101):
    cnt += i
    s_cnt += i * i
#    print(s_cnt)
print(pow(cnt,2))
print(s_cnt)
print(pow(cnt,2) - s_cnt)
print("------- ---------- ----------- -------- ---------- ----- ------ ---------- ------ ---- --- ----")


