class Bank:
    def __init__(self):
        self.accno = 10
        self.name = "vinod"
        self.balance = 10000.00
        self.__loan = 2000000.00
    def display(self):
        print(self.accno,"\n",self.name,"\n",self.balance)

a = Bank()
a.display()
print(Bank.__dict__)
print(a.__dict__)
