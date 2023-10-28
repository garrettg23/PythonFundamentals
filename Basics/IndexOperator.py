# index operator [] = gives access to a sequences's element (str, list, tuples)

name = "joe Shmoe"

# fix first name not capitalized, and print it
if name[0].islower():
    name = name.capitalize()

print(name)

# Test - Run this code below and describe what these two operators do.
first_name = name[:3].upper()
print(first_name)

last_name = name[4:].lower()
print(last_name)

# Answer: The first_name variable uses the index operator with function upper to
# return the first 3 characters in all upper case.
# The last_name does the same, but uses returns the last name in lower case
# Change the values in the operator like 3 and 4 to n and n + 1 characters
# that are contained in the first name ie. Sarah = 5 characters.

# Extra: access the last / first character in the string
last_character = name[-1]
print(last_character)

first_character = name[0]
print(first_character)
