from arithmetic import add,mul
from string_ops import reverse,vowel

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
print("Addition:",add(a,b))
print("Multiply:",mul(a,b))

s=input("Enter String ")
print("Reverse string :",reverse(s))
print("count vowel:",vowel(s))
