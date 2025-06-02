a = (1 , 20 , 30 , "Sumit" , "niku")

print(a)

b = a.count("Sumit")
c = a.count(1)
print(b,c)

t = (4, 5, 6, 5)
print(t.index(5))  # Output: 1
a, b = (1, 2)
print(a, b)  # Output: 1 2

t = (1, 2, 3)
print(2 in t)  # Output: True


for item in (10, 20, 30):
    print(item)

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)      # Output: (1, 2, 3, 4)
print(t1 * 3)       # Output: (1, 2, 1, 2, 1, 2)
