n=int(input("enter a number ")) 
i=0 
while i<n: 
    if n>0: 
        i+=1 
        print(' '*(n-i) + '* '*(i)) 
else: 
    print("enter a positive number")
