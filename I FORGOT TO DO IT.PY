import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Example usage
r = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(r)
print("The circumference of the circle is:", circumference)
