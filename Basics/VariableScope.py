# variable scope = the region that a variable is recognized.
# a variable is only available from inside the region it is createed.
# a global and locally scoped versions of a variable can be created.

# Two main types of variable scope: local and global
# Local Scope: Variables defined within a function are considered to have local scope.
# They are only accessible within that specific function and are not visible outside of it.
#
# Global Scope: Variables defined at the top level of your code or at the module level have global scope.
# They are accessible throughout the entire module or script.
#
# Python follows this order of operations when it comes to variables: LEGB
# L: Local - defined in a function
# E: Enclosing - this is in nesting, calls the inner most local variable first
# G: Global - defined at module level
# B: Built-in - predefined in python or imported to a module ... ex. import math -> print(math.sqrt(25)

first_name = "Joe"  # global scope (available inside &  outside of functions


def display_name():
    first_name = "Schmoe"  # local scope (available only inside this function))
    print(first_name)


print(first_name)
display_name()
