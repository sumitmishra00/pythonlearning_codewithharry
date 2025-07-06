class Employee:
    name = "Sumit"
    language = "py"  #class attribute
    salary = 1800000

sumit = Employee()

sumit.name = "Sumit" # object or instance attribute

print(sumit.name, sumit.salary,  sumit.language)

# here name is object attribute and salary and language
# is class attribute as they directly belong to class
