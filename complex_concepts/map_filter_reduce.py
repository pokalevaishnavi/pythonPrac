from functools import reduce

#map
nums = [2,3,6,2,55,12,3]

def sq(x):
    return x * x

n = list(map(sq,nums))
print(n)


#or

m = list(map(lambda x:x*x,nums))
print(m)

#filter

def is_greater_then_9(x):
    if(x>9):
        return True
    else:
        return False
    
nums = [2,3,6,2,55,12,3]
new = list(filter(is_greater_then_9,nums))
print(new)


#reduce

a = [1,2,3,4,5,6]

def sum(a,b):
    return a+b

c = reduce(sum,a)
print(c)