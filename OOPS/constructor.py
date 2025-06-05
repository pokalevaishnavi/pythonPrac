

class Employee:
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"{self.name} has {self.salary} salary and bond of {self.bond} years")
    
e1 = Employee(34000,"John Doe", 4)
    
print(e1.get_salary(),"/n",e1.get_info())