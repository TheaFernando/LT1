# Circular Garden Program
## Description:
### - Finding the needed information about the garden for the school.
## All five stages of CT (Computational Thinking):
### Problem Identfication: Find the Area (with estimation, then rounded up and down), Circumference, and square root.
### Problem Decomposition: First get the radius. Then separate the things we have to solve which are circumference, area, square root, area rounded up, and area rounded down. Lastly, display each with the required metric units.
### Pattern recognition: We can get the things we have to solve from one another. For example, we can get the square root using the area.
### Data representation: Text
### Algorithm Development:
~~~ 
Import math
Input radius
Assign area = math.pi * pow(radius, 2)
Assign circumference = 2 * math.pi * radius
Assign areaSquareRoot = math.sqrt(area)
Assign areaRoundDown = math.floor(area)
Assign areaRoundUp = math.ceil(area)
Output print(f"Area of the garden: {area:.2f} square meters.")
Output print(f"Circumference of the garden: {circumference:.2f} meters.")
Output print(f"Square root of the garden: {areaSquareRoot:.2f}")
Output print(f"Are rounded down: {areaRoundDown} square meters.")
Output print(f"Area rounded up: {areaRoundUp} square meters.")
~~~

## How to run:
 - Open "LT1," then click on the python labelled "CircularGarden.py."
## Input needed:
 - Radius
## Output sample:
~~~
Enter the radius: 5
Area of the garden: 78.54 square meters.
Circumference of the garden: 31.42 meters.
Square root of the garden: 8.86
Are rounded down: 78 square meters.
Area rounded up: 79 square meters.
~~~

### Author: Thea Margaux M. Fernando
### Section: 8-Sampaguita
