import random 
n = random.randint(1, 100)
a = -1
guesses = 1
while(a !=n):
          a= int(input("Guess The Lumber: "))
          if(a>n):
                  print("Lower Number Please")
                  guesses +=1
          elif(a<n):
                  print("Higher Number Please")
                  guesses +=1

print(f"You Have Guess The No.{n} Correctly in {guesses} Attempts")