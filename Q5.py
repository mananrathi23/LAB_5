num1 = int(input("enter the number:))
num2 = int(input("enter the number:))
a =num1
b =num2
while num1 != num2:
  if num1 > num2:
    num1 -= num2
  else:
    num2 -= num1
lcm = (a*b)//num1
print("lcm of ",a, " and ",b, " is ",lcm)
    
