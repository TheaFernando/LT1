# This library is to define predefined terms such as math.fmod(), and etc,.
import math

# We use input float to be able to display the radius in decimals.
radius = float(input("Enter the radius: "))

# This is the processing stage where we find the needed formulas to solve for the problems.
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius
areaSquareRoot = math.sqrt(area)
areaRoundDown = math.floor(area)
areaRoundUp = math.ceil(area)

# Finally, the output stage where we will display our results from the processing stage in square meters/meters.
print(f"Area of the garden: {area:.2f} square meters.")
print(f"Circumference of the garden: {circumference:.2f} meters.")
print(f"Square root of the garden: {areaSquareRoot:.2f}")
print(f"Are rounded down: {areaRoundDown} square meters.")
print(f"Area rounded up: {areaRoundUp} square meters.")