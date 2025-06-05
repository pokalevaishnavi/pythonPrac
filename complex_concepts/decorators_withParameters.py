def repeat(n):
    def decorator(f):
        def wrapper():            
            for i in range(n):
                f()
        return wrapper
    return decorator

@repeat(3)
def hello():
 print("Helloo world!")
 
 
hello()