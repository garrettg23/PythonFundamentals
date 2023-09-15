# Here is a sample of a few basic math functitons supported in
# base python or imported from the math module

import math

pi = math.pi
radius = 5
diameter = 2*radius
area = pi*(radius ** 2)

print(round(pi)) # Rounds to nearest whole integer
print(math.ceil(pi)) # Rounds up to next integer
print(math.floor(pi)) # Rounds down to next integer
print(abs(-pi)) # Prints absolute value (of neg pi)
print(pow(pi,2)) # This does pi to the power of 2, ie. squared
print(pi ** 3) # This does the same, pi to the power of 3 / pi cubed
print(math.sqrt(144)) # Does square root of a number
print(144 ** (1/2)) # Also does square root
print(max(pi, radius, diameter, area)) # prints the max value of the variables listed
print(min(pi, radius, diameter, area)) # prints the min value of the variables listed
