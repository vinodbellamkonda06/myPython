emp = {}
class Employee:
    num_of_emp = 0

    def __init__(self, name, id, age, salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary
        Employee.num_of_emp += 1


    def add_employee(self):
        emp[self.id] = self.id#l.append(self.id)
        emp[self.name] = self.name
        emp[self.age] = self.age
        emp[self.salary] = self.salary


    def display_employee(self,id):
            print("name:",emp[self.name])
            print("id:",emp[self.id])
            print("age:",emp[self.age])
            print("salary:", emp[self.salary])
    def delete_employee(self,id):
        pass
    def open(self):
        pass

    @classmethod
    def modify(cls,insentives):
        pass


emp1 = Employee("adithya",1,22,20000)
emp1.add_employee()
emp1.display_employee(1)
emp2 = Employee("ohh",2,22,20000)
emp2.add_employee()
emp2.display_employee(2)
emp3 = Employee('oo',3,23,8990)
print(Employee.num_of_emp)



