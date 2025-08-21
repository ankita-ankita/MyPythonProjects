# Factorial calculation

num = int(input ("enter the number for which you want factorial number of that: "))
fact = 1

for i in range (1,num+1):
 fact *= i

print("Factorial answer to your number us: ", fact)  
