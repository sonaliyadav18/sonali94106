def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))

while True :
    print("\n 1.add \n 2.subtract \n 3.multiply \n 4.divide \n 5.exit")
    choice=int(input("Enter choice :"))
    
    match choice:
        case 1:
              print("addition :",add(a,b))
        case 2:
              print("subtract :",sub(a,b))     
        case 3:
              print("multiply :",mul(a,b))      
        case 4:
              print("division :",div(a,b))
        case _:
              print("Invalid choice")
            
    
    
