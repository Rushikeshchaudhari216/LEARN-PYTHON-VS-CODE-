# f = open("file.txt")

# print(f.read())

# f.close()

# The same can be written using with statementlike this
with open("file.txt") as f :
          print(f.read())

# You dont need to f.close() 