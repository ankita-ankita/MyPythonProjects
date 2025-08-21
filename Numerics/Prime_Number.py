# Prime Check

num = int(input("Enter the number you want to check if it is prime: "))

for i in range (2,num):
 if num % i:
  a = "Prime Number"
 else:
  a = "Not a Prime Number"
  break 

print(a)     
