import random


while True:
    # Get a random number
    secret = random.randint(1, 6)


    # Ask the user for a guess
    guess_text = input("Pick a number between 1 and 6: ")
    guess = int(guess_text)


    # Check if they are the same
    if guess == secret:
        print("You guessed the number correctly!")
    else:
        print(f"You did not get it. The number was {secret}")