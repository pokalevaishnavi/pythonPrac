
while True:
    try:
        a = int(input("Enter num1 :"))
        b = int(input("Enter num2 :"))

        print(f"The sum is {a+b}")
        
    except Exception as e :
        print("Some error occured",e)