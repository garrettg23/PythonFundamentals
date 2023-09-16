# if statement = a block of code that will execute if it's condition is true.

age = int(input("How old are you?: "))

if age < 21 and age >= 18:
    print("You are an adult, but cannot legally drink yet.")
elif age >= 21:
    print("You can now legally have a beer.")
else:
    print("You are a child.")
