
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b 
def calculate(x, y, operation):
    return operation(x, y)
def display(name="User", message="Welcome"):
    print(message, name)
display()
display("Sonali")
display(name="Sonali", message="Good Morning")
display(message="Hello", name="Student")
a = 10
b = 5
print("Addition:", calculate(a, b, add))
print("Subtraction:", calculate(a, b, subtract))
print("Multiplication:", calculate(a, b, multiply))
print("Division:", calculate(a, b, divide))



