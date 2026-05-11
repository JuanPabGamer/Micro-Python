# TimesTableJP
# This program asks the user for a positive integer
# and prints the multiplication table from 10 to 20
# using a while loop.

# Ask the user for a positive integer
number = int(input("Enter a positive integer: "))

# Starting value
count = 10

# While loop from 10 to 20
while count <= 20:
    # Print the multiplication result
    print(number, "x", count, "=", number * count)
    
    # Increase count by 1
    count = count + 1
