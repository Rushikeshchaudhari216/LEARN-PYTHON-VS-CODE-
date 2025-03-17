from functools import reduce
l = [34,45,66,78,45,33,56,78,100,36,123,44,90]

def greater(a, b):
          if (a>b):
                  return a
          return b

f = reduce(greater, l)
print(f)