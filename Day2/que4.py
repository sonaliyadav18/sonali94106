def prime(n):
    if n <= 1:
      return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
          return False
    return True

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if prime(num):
      print(num)


    
