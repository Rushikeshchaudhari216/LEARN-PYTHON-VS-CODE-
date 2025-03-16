f = open("poem.txt")
content = f.read()

if("twin  kle" in content):
          print("The word is present in the content")
else:
        print("The word is not present in the content")

f.close()