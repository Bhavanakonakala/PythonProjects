# This program converts radians into degrees
import math
def radians_to_degrees(angle_in_radians):
    # Using the formula: degrees = radians * (180 / pi)
    degrees = angle_in_radians * (180.0 / math.pi)
    return degrees
angle_in_radians = float(input("Please enter your angle :"))  # Replace this with any angle in radians that you want to convert
degrees = radians_to_degrees(angle_in_radians)
print(f"{angle_in_radians} radians is equal to {degrees} degrees.")

