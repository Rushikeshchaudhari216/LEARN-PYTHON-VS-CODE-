class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


rushi = Employee()
rushi.name = "Rushi" # This is an instance attribute
print(rushi.name, rushi.language, rushi.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class