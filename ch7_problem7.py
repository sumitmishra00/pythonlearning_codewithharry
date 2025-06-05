# pattern prob 1 n =3
'''
  *
 ***
*****
''' 

n = int(input("enter number: "))


for i in range(1, n+1):   #i is number of row 

    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")
