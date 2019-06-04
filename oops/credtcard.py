class Employe:
    def __init__(self,name,id,salary,age):
        self.name = name
        self.id = id
        self.salary = salary
        self.age = age

    def display(self):
        pass
    @classmethod
    def modify(cls,insentives):
        pass


emp1 = Employe()
emp1.dispaly("vinod",1,1000,22)