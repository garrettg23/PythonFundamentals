# return statement = Functions send Python values/objects back to the caller.
# These values/objects are known as the functions return value
# Use return in a Python function when you want the function to calculate a value and provide that value back to the
# calling code, whereas use print when you want to display a value to the console for informational or debugging
# purposes, without necessarily returning a value from the function

def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 8)

print(x)

# notice how this does not print anything:
multiply(5, 7)

# but, this will.
print(multiply(5, 7))

# same thing without return, using print instead.
def multiply2(number1, number2):
    print(number1 * number2)


multiply2(9, 16)
