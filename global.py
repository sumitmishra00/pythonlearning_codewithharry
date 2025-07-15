a = 44

def func():
    global a

    a = 5

    print(a)

func()
print(a)