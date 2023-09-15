# User input: how to accepts user input for variables/etc.

# User input is always accepted as a string data type, so you need to cast if you want to do math

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = input("How old are you?: ")

print("Hello, "+first_name+" "+last_name)
print("Next year you will be "+str(int(age) + 1)+" years old!")

# Another note - you can cast the input as well:
age = int(input("How old are you?: "))
