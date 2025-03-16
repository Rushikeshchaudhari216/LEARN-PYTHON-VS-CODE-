class Employee:
          company = "TESLA"
          name = "Default name"
          def show(self):
                  print(f"The Name Is {self.company} & The Company Is {self.company}")

class coder:
        language = "python"
        def printLanguages(self):
                print(f"out of all languages is here your language:{self.language}")

class programmer(Employee, coder):
        company = "TESLA CYBERTRUCK"
        def showLanguage(self):
                print(f"The Name Is {self.company} & The Language Is {self.language}")


a = Employee()
b = programmer()

b.show()
b.printLanguages()
b.showLanguage()