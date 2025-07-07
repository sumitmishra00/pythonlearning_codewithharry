class employee:
    company = "XYZ"

    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

# class programmer:
#     company = "XYZ Info "
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def showLanguage(self):

#         print(f"the name is {self.name} and he is good with {self.language} language")


class programmer(employee):
    company = "XYZ Info "
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.labguage} language")

a = employee()

b = programmer()

print(a.company , b.company)

