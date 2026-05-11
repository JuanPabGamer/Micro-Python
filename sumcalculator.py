
# SumCalculatorJP
# This program asks the user for a positive integer
# and calculates the sum of all integers from 0
# up to the user number using a while loop.

# Ask the user for a positive integer
number = int(input("Enter a positive integer: "))

# Variables for the loop
count = 0
total = 0

# While loop to calculate the sum
while count <= number:
    total = total + count
    count = count + 1

# Display the final sum
print("The sum of the numbers from 0 to", number, "is:", total)
