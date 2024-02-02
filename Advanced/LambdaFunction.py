# lamda function = function written in  line using lambda keyword
# accepts any numberr of arguments, but only has one expression
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lamda parameterrs:expression

double = lambda x: x * 2
print(double(2))

multiply = lambda x, y: x * y
print(multiply(3,8))

add = lambda x, y, z: x + y + z
print(add(5,7,2))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Joe","Schmoe"))

age_check = lambda age: True if age >= 21 else False
print(age_check(23))
