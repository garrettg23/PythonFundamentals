# str.format() = optional method that gives users more control when displaying output

number = 10000

print("The number pi is {:.3f}".format(number))  # 3 decimal places
print("The number is {:,}".format(number))  # standard number formatting with commas
print("The number is {:b}".format(number))  # binary
print("The number is {:o}".format(number))  # octal aka base-8
print("The number is {:X}".format(number))  # hexadecimal aka base 16
print("The number is {:E}".format(number))  # Exponential

print("The {animal} jumped over the {item}.".format(animal="cow", item="moon"))  # keyword argument version of below

animal = "cow"
item = "moon"

print("The {} jumped over the {}.".format(animal, item))
print("The {0} jumped over the {1}.".format(animal, item))  # Positional Argument

text = "The {} jumped over the {}."
print(text.format(animal, item))  # annoying

print(f"The {animal} jumped over the {item}.")  # This doees the same

# you can also pad strings and align them as well
name = "Joe"

print(f"Hello, my name is {name:10}. Nice to meet you")  # left align the padding
print(f"Hello, my name is {name:>10}. Nice to meet you")  # right align with padding
print(f"Hello, my name is {name:^10}. Nice to meet you")  # center align the padding
