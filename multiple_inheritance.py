class employee:
    company = "XYZ"
    name = "Stark"

    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")

class coder:
    language = "python"
    def printLanguage(self):
        print(f"out of all language here is your language : {self.language}")


class programmer(employee, coder):
    company = "XYZ Info "
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")

a = employee()

b = programmer()

b.show()

b.showLanguage()

b.printLanguage()


