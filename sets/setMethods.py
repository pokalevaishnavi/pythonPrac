# add() – Adds a single element to the set
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}

# update() – Adds multiple elements (from iterable) to the set
s = {1, 2}
s.update([3, 4])
print(s)  # {1, 2, 3, 4}

# remove() – Removes the specified element (raises error if not found)
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

# discard() – Removes the specified element (does nothing if not found)
s = {1, 2, 3}
s.discard(4)
print(s)  # {1, 2, 3}

# pop() – Removes and returns an arbitrary element
s = {10, 20, 30}
x = s.pop()
print(x)      # 10 (or any random element)
print(s)      # Remaining elements

# clear() – Removes all elements from the set
s = {1, 2, 3}
s.clear()
print(s)  # set()

# union() – Returns a new set with all elements from both sets
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# intersection() – Returns a new set with only common elements
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}

# difference() – Returns elements in set A but not in B
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}

# symmetric_difference() – Elements in either A or B but not both
a = {1, 2, 3}
b = {2, 4}
print(a.symmetric_difference(b))  # {1, 3, 4}

# issubset() – Checks if set A is subset of B
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# issuperset() – Checks if set A is superset of B
a = {1, 2, 3}
b = {2, 3}
print(a.issuperset(b))  # True

# isdisjoint() – Checks if two sets have no elements in common
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True

# copy() – Returns a shallow copy of the set
s = {1, 2, 3}
new_s = s.copy()
print(new_s)  # {1, 2, 3}
