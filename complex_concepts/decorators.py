def decorator(f):
    def wrapper():
        print("function is gonna execute..")
        f()
        print("function is gonna execute..")
    return wrapper

@decorator
def hello():
 print("Helloo world!")
 
 
hello()


