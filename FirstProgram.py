

# 2nd lasrgest element
'''
def num(a):
    b = sorted(a)
    print(b)
    count = -2
    for num in a:
        if b[count] < b[count+1]:
            print(b[count])
            return
        if b[count] == b[count+1]:
            count = count - 1   
    

a = [2,6,5,1,4,8,4,3,2]
num(a)
'''



'''
#remove dups
a = [1, 2, 2, 3, 4, 4, 5]

a = list(set(a))

print(a)
'''
#flatten list

'''
def flatten_list(l1):
    l2 = []
    for sublist in l1:
        print(sublist)
        if isinstance(sublist, list):
            l2.extend(sublist)
            print('extended',l2)
        else:
            l2.append(sublist)
            print('appended',l2)
    return l2

a = ([1,2],[3,4],5)
b = flatten_list(a)

# print(a)
print('final',b)
'''
