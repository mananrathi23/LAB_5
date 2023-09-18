count = int(input("How many numbers you want to take HCF: "))
while count <= 0 :
    print("Invalid input")
    count = int(input("How many numbers you want to take HCF: "))
num=int(input("enter number 1:"))    
while num<=0:    
    print("Invalid input")
    n=int(input("enter number 1:"))

i = 1
while i < count:
    n = int(input(f"Enter number {i+1}: "))
    if n <=0:
        print("Invalid input")
        n = int(input(f"Enter number {i+1}: "))
    else:
        while n:
            temp=num
            num=n
            n=temp%n  
        i += 1
print(f"HCF of given numbers is {num}")
