'''
print("Hello Vaishnavi!")

a = 50;
b = "Vaishnavi"
c= 100

print(b," has ",a," marks out of ",c)
print(f"{b} has {a} marks out of {c}")
'''



'''
strng = "We can perform various operations"
for(int i = 0, i<strng.length; i++):

	
strng = "We can perform various operations"
strng3 = reverse(strng)
print(strng3)
'''

dict1 = [{'Name':'Vaishnavi','uniqueId':111,'Age':20},
         {'Name':'Varada','uniqueId':222,'Age':13},
         {'Name':'Soham','uniqueId':333,'Age':14}]

# a = tuple(dict1.keys())
# b = tuple(dict1.value())

for i in dict1:
    print(f"{i['Name']:10}{i['uniqueId']:20}{i['Age']:10}")


list1 = [2,3,4,5,6,7,8,9,12,11]
map(lambda x : x**2 ,list1)
print(list1)
list(map(lambda x : x**2 ,list1))
