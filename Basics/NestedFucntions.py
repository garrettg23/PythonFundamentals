# nested function calls = function calls inside other function calls. inner most function calls are resolved first.
# returned value is used as arugment for the next outer function

# example with physically defined nested function
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


outer_function(6)(7)
result = outer_function(5)(3)  # This calls inner_function with x=5 and y=3
print(result)

# example with various pre defined functions - input any real number, converts to floating point, absolute value,
# and finally rounds it to the nearest whole number

print("The absolute value of the number you picked rounded to the nearest whole number is " + str(round(abs(float(input("Enter any real number: "))))))

# The above does the same as all of these lines of code commented out below
#
# num = input("Enter any real number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print("The absolute value of the number you picked rounded to the nearest whole number is "+ str(num))
