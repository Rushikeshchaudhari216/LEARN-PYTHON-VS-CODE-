import random

# Computer choice and dictionaries for mapping
computer = random.choice([1, 2, 3])
youdict = {"s": 1, "w": 2, "g": 3}
reversedict = {1: "snake", 2: "water", 3: "gun"}

# Get user input
youstr = input("Enter Your Choice (s for snake, w for water, g for gun): ")

# Check if the user input is valid
if youstr not in youdict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youdict[youstr]  # Get the user's choice as a number
    
    # Display choices
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")

    # Determine the outcome of the game
    if computer == you:
        print("Draw Match")
    elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
        print("Oops! You lose.")
    else:
        print("Congratulations! You win.")

    # End the game with a message
    print("The End. Thank you for playing!")