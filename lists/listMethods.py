# append() – Adds an item to the end of the list
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# extend() – Appends elements from another iterable
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]

# insert() – Inserts an element at a given position
lst = [1, 3]
lst.insert(1, 2)
print(lst)  # [1, 2, 3]

# remove() – Removes the first occurrence of a value
lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)  # [1, 3, 2]

# pop() – Removes and returns item at given index (last by default)
lst = [1, 2, 3]
x = lst.pop()
print(x)    # 3
print(lst)  # [1, 2]

# clear() – Removes all elements from the list
lst = [1, 2, 3]
lst.clear()
print(lst)  # []

# index() – Returns the index of the first occurrence of a value
lst = [10, 20, 30, 20]
print(lst.index(20))  # 1

# count() – Counts how many times an element appears
lst = [1, 2, 2, 3, 2]
print(lst.count(2))  # 3

# sort() – Sorts the list in ascending order (modifies original list)
lst = [3, 1, 4, 2]
lst.sort()
print(lst)  # [1, 2, 3, 4]

# sort(reverse=True) – Sorts the list in descending order
lst = [3, 1, 4, 2]
lst.sort(reverse=True)
print(lst)  # [4, 3, 2, 1]

# reverse() – Reverses the elements in place
lst = [1, 2, 3]
lst.reverse()
print(lst)  # [3, 2, 1]

# copy() – Returns a shallow copy of the list
lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)  # [1, 2, 3]
