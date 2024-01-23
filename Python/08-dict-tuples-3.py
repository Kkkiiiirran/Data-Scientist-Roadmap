PI = 3.14

def circle_calc():
    radius = float(input("Enter the radius"))
    diameter = round(2* radius, 3)
    circumference = round(PI * diameter, 3)
    area = round(PI * (radius*radius), 3)

    return(diameter, circumference, area)

print(circle_calc())

import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

