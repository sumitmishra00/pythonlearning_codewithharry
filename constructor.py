class employee:
    language = "python"
    salary = 1200000

    def __init__(self , name , salary , language): #dunder method which is automatically called

        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

sumit = employee("Sumit" , "javascript" , 1500000)

# sumit.name = "Sumit"

print(sumit.name, sumit.salary , sumit.language)

