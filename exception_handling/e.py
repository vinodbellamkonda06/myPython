class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg

def check(dict):
    for k, v in dict.items():
        print('name={:15s} balance= {:10.2f}'.format(k, v))
        #print('name={:} balance= {:}'.format(k, v))
        if (v < 2000):
            raise MyException('balance amount is less for' +k)
bank = {'raj':20000, 'vani':1000}
try:
    check(bank)
except MyException as e:
    print(e)






