try:
    a = int(input("hey, enter a number:"))
    print(a)


except Exception as e:
    print(e)

finally:

    print("I am inside finally")

    