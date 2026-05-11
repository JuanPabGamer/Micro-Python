# GuessAreaRectangleYourName
# This program asks the user for the length, width,
# and guessed area of a rectangle.

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

guess = float(input("Enter the area: "))

# Calculate the correct area
area = length * width

# Check if the guess is correct
if round(guess, 2) == round(area, 2):
   print("Correct! The area is", round(area, 2))
else:
   print("Incorrect.")
   print("The correct area is", round(area, 2))
