# variable = a container for a value. Behaves as the value that it contains.
# Data types included: string, integer, float, and boolean

# string data type variable.
first_name = "Garrett"
last_name = "Galarneau"
print("Hello "+first_name+" "+last_name)

#How to check data type of variable. <class 'str'> = string.
print(type(first_name))

# integer data type variable.
age = 26

# say it is your birthday, let's add 1 to you age.
# you could write it like this: age = age + 1
# but this is faster:
age += 1

print(age)
print(type(age))

# Showcasing data type importance, cannot use math with strings without casting.
new_age = "26"
## new_age += 1
# this would fail without casting string to int before adding:
# Fixed Version:
new_age = int(new_age)
new_age +=1
print(new_age)

#Let's display our name next to our name variable.
print("Hello, "+first_name+". On your next birthday you will be "
      +str(new_age)+"!")

# floating point number variable ie. float.
height = 69.5
print("You are "+ str(height) + " inches tall!")
print(type(height))

# boolean data type variable, true or false.
birthday = False
print("Is today your birthday? " + str(birthday))
print(type(birthday))
