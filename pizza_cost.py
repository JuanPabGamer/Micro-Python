# Constants
HST = 0.13
LABOUR = 0.75
MATERIAL = 0.5
RENT = 1.0

print("Let's calculate the cost of your pizza")

# Get input from the user (and convert it to a number)
diameter = float(input("What is the diameter (in)? "))

# Perform calculations
total_material_cost = diameter * MATERIAL
subtotal = RENT + LABOUR + total_material_cost
tax = subtotal * HST
total = subtotal + tax

# Round to 2 decimal places and print
print("The cost of your pizza is $" + str(round(total, 2)))