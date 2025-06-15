def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
         return c
        

a = 2
b = 5
c = 12 

print(greatest(a , b , c))
