class Employee:
    company = "TCS"
    def __init__(self,name):
        self.name = name
    
    #static method
    # doesnt pass self/obj as parameter
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def changeName(cls,ncompany):
        cls.company = ncompany
    
e = Employee("Varada")

print(e.sum(2,3))
print(e.company)
e.changeName("BenchMark")
print(e.company)
    