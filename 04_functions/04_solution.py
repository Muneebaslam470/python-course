import math

def circle_stat(radius):
    Area = math.pi * radius**2
    circumference = 2* math.pi *radius
    return Area, circumference

a , c = circle_stat(23)
print(round(a,2) ,round(c,2))
