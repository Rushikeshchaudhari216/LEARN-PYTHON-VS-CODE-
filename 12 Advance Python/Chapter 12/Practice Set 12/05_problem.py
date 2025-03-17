n =int(input("Enter The No."))

table = [n*i for i in range(1, 11)]
with open ("tables.txt", "a") as f:
          f.write(f"Table Of {n}: {str(table)} \n")