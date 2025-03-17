def divisible5(n):
          if(n%5 == 0):
                  return True
          return False
a =[4,5,25,66,78,79,99,85,65,60,20]
f = list(filter(divisible5, a))
print(f)