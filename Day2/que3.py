def fab(num):
  a=0
  b=1 
  print(a)
  print(b)
  for i in range(num):
    c=a+b
    print(c)
    a=b
    b=c
  return c

num=int(input("Enter number:"))
num=fab(num)

    
 