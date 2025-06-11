# Example of *args and **kwargs in Python

# Function using *args - accepts any number of positional arguments
def print_args(*args):
    # args is a tuple of positional arguments
    print("Positional arguments (args):")
    for arg in args:
        print(arg)

# Function using **kwargs - accepts any number of keyword arguments
def print_kwargs(**kwargs):
    # kwargs is a dictionary of keyword arguments
    print("Keyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Function using both *args and **kwargs
def print_all(*args, **kwargs):
    print("All arguments:")
    print("Positional arguments:")
    for arg in args:
        print(arg)
    
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Example usage
print_args('apple', 'banana', 'cherry')

print_kwargs(name='Alice', age=30, country='USA')

print_all('red', 'green', 'blue', size='large', shape='circle')
