#WAP to find out whether a student has passed or failed if it requires a total 40% and at least 33% in each subject to pass assume 3 subjects and take marks as an input from the user 

marks1 = int(input("enter your marks 1 : "))
marks2 = int(input("enter your marks 2 : "))
marks3 = int(input("enter your marks 3 : "))

total_percent = (100*(marks1 + marks2 + marks3))/300

if(total_percent>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Pass", total_percent)

else:
    print("fail",total_percent)    
    