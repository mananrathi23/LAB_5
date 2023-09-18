count = int(input("How many numbers you want to take lcm: "))
while count <= 0:
    print("Invalid input, please enter a positive value:")
    count = int(input("How many numbers you want to take lcm: "))

i = 1
lcm = 1
while i <= count:
    n = int(input(f"Enter number {i}: "))
    if n < 0:
        print("Invalid input, please enter positive integers.")
    else:
        a, b = lcm, n
        while b:
            temp=a
            a=b
            b=temp%b   
        lcm = (lcm * n) // a
        i += 1

print(f"LCM of given numbers is {lcm}")
