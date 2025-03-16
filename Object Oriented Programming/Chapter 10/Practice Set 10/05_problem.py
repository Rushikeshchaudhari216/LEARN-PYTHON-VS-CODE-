from random import randint

class Train:
          def __init__(self, trainNo):
                  self.trainNo = trainNo

          def book(self, fro, to):
                  print(f"Ticket Is Book In Train NO: {self.trainNo} from {fro} to {to}")

          def getStatus(self):
                  print(f"Train NO: {self.trainNo} Is Running on Time")

          def getFare(self, fro, to):
                  print(f"Ticket Fare In Train NO: {self.trainNo} from {fro} to {to} is {randint(111, 9999)}")
t = Train(12399)
t.book("Nashik", "Pune")
t.getStatus()
t.getFare("Nashik", "Pune")