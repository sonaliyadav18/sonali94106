def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input("Enter a : "))
b = int(input("Enter b :"))

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Result:", add(a, b))
        case 2:
            print("Result:", subtract(a, b))
        case 3:
            print("Result:", multiply(a, b))
        case 4:
            print("Result:", divide(a, b))
        case _:
            print("Invalid choice! Please try again.")
