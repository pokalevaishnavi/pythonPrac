'''
 Instance attributes are unique to each object and are set via the constructor, while class attributes are shared across all instances of a class. This lesson covers how to define and use both types of attributes to manage data at the object and class levels.
'''



class Employee:
    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        return(f"{self.name} has {self.salary} salary and bond of {self.bond} years")
    
e1 = Employee(34000,"John Doe", 4, "Tesla")
    
print(e1.company,"\n",e1.get_info())#will always print instance if present



#obj introspection : objs in class

print(dir(e1))