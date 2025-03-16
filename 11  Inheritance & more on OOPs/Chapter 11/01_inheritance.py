class Employee:
          company = "TESLA"
          def show(self):
                  print(f"The Name Is {self.name} & The Salary Is {self.salary}")

class programmer:
        company = "TESLA CYBERTRUCK"
        def show(self):
                print(f"The Name Is {self.name} & The Salary Is {self.salary}")

        def showLanguage(self):
                print(f"The Name Is {self.name} & The Salary Is {self.salary}")

        def show(self):
                print(f"The Name Is {self.name} & He Is Good In {self.Language} Language")

a = Employee()
b = programmer()

print(a.company, b.company)