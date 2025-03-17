a = 1111 #Global Variable

def fun():
          global a
          a = 2222
          print(a)

fun()
print(a)