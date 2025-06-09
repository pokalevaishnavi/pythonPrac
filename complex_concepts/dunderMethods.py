#dunder : duoble underscore methods


# Object Creation and Initialization

class Person:
    # __init__ is called when a new instance is created (constructor)
    def __init__(self, name):
        self.name = name

    # __new__ is called before __init__, used to control object creation (rarely needed)
    def __new__(cls, *args, **kwargs):
        print("Creating instance of Person")
        return super().__new__(cls)

print("\n--- Object Creation ---")
p = Person("Alice")
print(p.name)  # Output: Alice


# String Representation

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # __str__ is used by str() and print(), meant for human-readable output
    def __str__(self):
        return f"{self.name} costs ${self.price}"

    # __repr__ is used by repr(), meant for unambiguous representation (debugging)
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

print("\n--- String Representation ---")
prod = Product("Book", 19.99)
print(str(prod))   # Output: Book costs $19.99
print(repr(prod))  # Output: Product(name='Book', price=19.99)


# Arithmetic Operators

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __str__(self):
        return str(self.value)

print("\n--- Arithmetic Operators ---")
a = Number(10)
b = Number(5)
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0


# Comparison Operators

class Box:
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

print("\n--- Comparison Operators ---")
box1 = Box(10)
box2 = Box(15)
print(box1 == box2)  # Output: False
print(box1 < box2)   # Output: True
print(box1 >= box2)  # Output: False


# Container Behavior

class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

print("\n--- Container Behavior ---")
ml = MyList()
ml.data = [10, 20, 30]
print(ml[1])     # Output: 20
ml[1] = 50
print(ml[1])     # Output: 50
del ml[1]
print(ml.data)   # Output: [10, 30]
print(len(ml))   # Output: 2
print(30 in ml)  # Output: True


# Callable Object

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

print("\n--- Callable Object ---")
greet = Greeter("Bob")
print(greet())  # Output: Hello, Bob!


# Context Manager

class FileManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

print("\n--- Context Manager ---")
with FileManager():
    print("Inside context")

# Output:
# Entering context
# Inside context
# Exiting context


# Attribute Access

class Demo:
    def __getattr__(self, name):
        return f"'{name}' not found"

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f"Deleting attribute {name}")
        del self.__dict__[name]

print("\n--- Attribute Access ---")
d = Demo()
d.x = 10          # Setting x to 10
print(d.x)        # 10
print(d.y)        # 'y' not found
del d.x           # Deleting attribute x


# Object Destruction

class A:
    def __del__(self):
        print("Object of class A is being deleted")

print("\n--- Object Destruction ---")
a = A()
del a  # Output: Object of class A is being deleted
