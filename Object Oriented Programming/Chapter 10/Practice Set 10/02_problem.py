class calculater:
          def __init__(self, n):
                  self.n = n
          def square(self):
                  print(f"The Square Is {self.n*self.n}")
          def cube(self):
                  print(f"The Cube Is {self.n*self.n*self.n}")
          def squareroot(self):
                  print(f"The Squareroot Is {self.n**1/2}")
a = calculater(4)
a.square()
a.cube()
a.squareroot()