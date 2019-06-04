
class A1(object):
    pass

class A2(object):
    pass

class A3(object):
     pass

class B(A1, A2):
    pass

class C(A3):
    pass

class D(B,C):
    pass

d1 = D()
print (D.__mro__)



class car:
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm
    def price_inc(self):
        self.price=int(self.price*1.15)
honda=car("city",100000,2017)
tata=car("bolt",600000,2016)
honda.cc=1500
print(honda.price)
print(tata.modelname)