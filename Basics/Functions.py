# function = a block of code which is executed only when it is called.

# use f strings in print statements from here on out instead of having to implicitly cast different data types to
# strings.

# for example - I will not repeat my code (no need to copy paste the print statement)
def repeat():
    print("I will not repeat my code!")


repeat()
repeat()
repeat()


# Each function defines parameters, needs matching number of arguments when called.
def hello(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}")
    print(f"You are {age} years old")


hello("Joe", "Shmoe", 32)
