class employee:
    language = "python"
    salary = 55000

    def getInfo(self):

        print(f"the language is {self.language}. The salary is {self.salary}")

sumit = employee()

sumit.language = "Javascript" 

sumit.getInfo()
