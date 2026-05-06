print("Let's calculate the area of a trapezoid")

# Taking inputs and converting them to floats for calculation
length = float(input("What is the length (m)? "))
width = float(input("What is the width (m)? "))
height = float(input("What is the height (m)? "))

# Calculating the area
area = (length + width) / 2 * height

# Displaying the result
print(f"Area of the trapezoid is {area}m^2")