num=int(input("Enter 5digit number:"))

original=num
rev=0
while num>0:
 digit=num%10
 rev=rev*10+digit
 num=num//10
 
if original==rev:
   print("No is pelidrome")
else:
   print("No is not pelidrome")