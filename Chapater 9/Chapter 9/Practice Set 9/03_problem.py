
def generateTable(n):
          table =""
          for i in range(1, 11):
                  table += f"{n} X {i} = {n*i}\n"

          with open(f"tables/table_{n}", "w") as f:
                  f.write(table)



for i in range(1, 21):
        generateTable(i)