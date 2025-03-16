st = "Hey Rushi, Men Are Brave."

with open("myfile.txt", "a") as f:
    f.write(st + "\n")  # Adds a new line after the content

# No need to explicitly close the file, 'with' handles that.
