try:
          a = int(input("Hey,Enter a number: "))
          print(a)

except Exception as e:
        print(e)

print("Thank You")

#ZeroDivisionError
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if(b == 0):
        raise ZeroDivisionError("Program Not Supported To Zero")
if(a == 0):
        raise ZeroDivisionError("Program Not Supported To Zero")
else:
        print(f"The division of a/b is {a/b}")