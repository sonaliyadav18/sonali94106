def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b): 
    return a * b
def div(a, b): 
    return a / b

def cal(op1, op2, operation):
    return operation(op1, op2)
 
a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
print("Addition :",cal(a, b, add))
print("Substract:",cal(a, b, sub))
print("Multiply:",cal(a, b, mul))
print("Division:",cal(a, b, div))
