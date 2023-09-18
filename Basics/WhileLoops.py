# While loop = a statement that will execute it's block of code,
# as long as it's condition remains true.

    # here is an example of an infiniite loop below... run if you dare.
    # there is no way to escape currently.

#while 1 == 1:
#    print("Help, I am stuck in a infinite loop! Kill the program!")

# various samples of name input examples below, if the user does not input name it will keep asking.
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)

name2 = None

while not name2:
    name2 = input("Enter your name: ")

print("Hello "+name2)
