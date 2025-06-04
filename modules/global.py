def sum(a,b):
    c = a+b
    global z 
    z = 0
    return c

z = 3
print(sum(2,3),z)