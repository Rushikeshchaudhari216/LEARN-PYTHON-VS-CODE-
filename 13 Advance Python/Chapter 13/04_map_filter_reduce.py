from functools import reduce
# Map Eexample
l =[1,2,3,4,5]
square = lambda a:  a*a
sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
          if(n%2 ==0):
                  return True
          return False
onlEven = filter(even, l)
print(list(onlEven))

# Reduce Example
def sum(a, b):
        return a + b
print(reduce(sum, l))