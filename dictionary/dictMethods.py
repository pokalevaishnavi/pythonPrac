# get() – Returns the value for the specified key, or None if not found
d = {'a': 1, 'b': 2}
print(d.get('a'))  # 1
print(d.get('c'))  # None

# keys() – Returns a view of all keys in the dictionary
d = {'a': 1, 'b': 2}
print(d.keys())  # dict_keys(['a', 'b'])

# values() – Returns a view of all values in the dictionary
d = {'a': 1, 'b': 2}
print(d.values())  # dict_values([1, 2])

# items() – Returns a view of key-value pairs (tuples)
d = {'a': 1, 'b': 2}
print(d.items())  # dict_items([('a', 1), ('b', 2)])

# update() – Updates dictionary with key-value pairs from another dict
d = {'a': 1}
d.update({'b': 2})
print(d)  # {'a': 1, 'b': 2}

# pop() – Removes and returns the value for a specified key
d = {'a': 1, 'b': 2}
val = d.pop('a')
print(val)  # 1
print(d)    # {'b': 2}

# popitem() – Removes and returns the last inserted key-value pair
d = {'a': 1, 'b': 2}
pair = d.popitem()
print(pair)  # ('b', 2)
print(d)     # {'a': 1}

# clear() – Removes all items from the dictionary
d = {'a': 1, 'b': 2}
d.clear()
print(d)  # {}

# setdefault() – Returns value of key, or inserts key with default value
d = {'a': 1}
val = d.setdefault('b', 2)
print(val)  # 2
print(d)    # {'a': 1, 'b': 2}

# copy() – Returns a shallow copy of the dictionary
d = {'a': 1}
d2 = d.copy()
print(d2)  # {'a': 1}

# fromkeys() – Creates a new dictionary from given keys and a default value
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}
