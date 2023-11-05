# keyword argument = named parameter passed to a function with its corresponding value, allowing you to specify the
# argument's value by name; they are used to make function calls more readable, self-documenting, and to provide
# flexibility when calling functions with optional or non-standard parameters.

def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}!")


# note you can switch up the arguments order compared to the parameters defined in the function
hello(last="Schmoe", middle="Doe", first="Joe")
