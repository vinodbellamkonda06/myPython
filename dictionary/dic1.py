qualifier = {"KKR": {'Chris Lynn': 4,
                      'Sunil Narine': 10,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Gautam Gambhir (c)': 12,
                      'Robin Uthappa (wk)': 1,
                      'Ishank Jaggi': 28,
                      'Colin Grandhomme': 0,
                      'Suryakumar Yadav': 31,
                      'Piyush Chawla': 2,
                      'Nathan Coulter-Nile': 6,
                      'Umesh Yadav': 2,
                      'Ankit Rajpoot': 4,
                      'Extra runs': 7,
                      'Total batted': 10},
                "MI": {'Lendl Simmons': 3,
                      'Parthiv Patel (wk)': 14,
                      'Ambati Rayudu': 6,
                      'Rohit Sharma (c)': 26,
                      'Krunal Pandya': 45,
                      'Kieron Pollard': 9,
                      'Extra runs': 8,
                      'Total batted': 6}}


k = qualifier["KKR"]
print(k)
m = qualifier["MI"]
#print(m)

k.pop("Total batted")
m.pop("Total batted")

print("score card of MI team:")
for name,score in m.items():
    pass
    #print(name , ":", score)

kkr_total = (sum(k.values()))
mi_total = (sum(m.values()))


print("Match result:")
if kkr_total < mi_total:
    print("MI team won the match:")
else:
    print("KKR team won the match:")


def sloppy_blowers(k_extra, m_extra):

    if k_extra > m_extra:
        print("KKR")
    else:
        print("MI")


sloppy_blowers(k_extra = k.keys(), m_extra = m.keys())


x = 4
k = 0
m = 0

for i in range(x):
    k += 1
    for j in range(x):
        m += 1
        print(j)
        x = 2

print(k, m)

d = {'a':[1,2,3], 'b':(4,5,6),'c':None}