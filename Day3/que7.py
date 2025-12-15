fact = lambda n: 1 if n == 0 or n == 1 else n * fact(n - 1)
pow = lambda b, p: b ** p

print(f"fact(5) = {fact(5)}")
print(f"pow(2,3) = {pow(2,3)}")