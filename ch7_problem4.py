#WAP to check whether the number is prime or not 

n = int(input("enter number: "))

for i in range(2,n):
    
    if(n%i) == 0:
        
        print("Number is not prime")
        
        break

else:

    print("number is prime")
