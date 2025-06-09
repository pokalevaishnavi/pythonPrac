
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        
    @property   
    def first_name(self):
        return self.name.split(" ")[0]
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        newName =f"{first} {l[1]}"
        self.name = newName
        
e = Employee("Jack Doe",34555)
# e.projects = 6
# print(e.projects)
print(e.name)
e.first_name = "Lala"
print(e.name)
    
    
# name = "vaishnavi/Manoj/Pokale"
# p = name.split("/")
# print(p)