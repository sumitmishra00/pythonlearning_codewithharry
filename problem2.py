# WAP to accept marks of 6 students and display them in a sorted manner

Students= []

s1 = int(input("enter marks of student 1 : "))
Students.append(s1)
s2 = int(input("enter marks of student 2 : "))
Students.append(s2)
s3 = int(input("enter marks of student 3 : "))
Students.append(s3)
s4 = int(input("enter marks of student 4 : "))
Students.append(s4)
s5 = int(input("enter marks of student 5 : "))
Students.append(s5)
s6 = int(input("enter marks of student 6 : "))
Students.append(s6)

Students.sort()
print(Students)
