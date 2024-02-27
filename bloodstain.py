# Code for problem 1 should go here
# To use trigonometry functions, you need to import the math module
# import math
# math.sin(x) returns the sine of x

# To get input from the user, use the input() function
# width = float(input("Enter bloodstain width: "))

import math
w= float(input("Enter the value of width:"))
l= float(input("Enter the value of length:"))
x= w/l
x_radians= math.asin(x)
x_degrees= math.degrees(x_radians)
print('the value of the angle in degree:', x_degrees)
#second
d= float(input("Enter the value of distance:"))
h_radians= math.tan(x_radians)
print('dotan', h_radians)
h= d*h_radians
print("the height that the bloodstain fell from:", h)
