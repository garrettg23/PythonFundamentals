# *args = parameter that will pack all arguments into a tuple.
# useful so that a functiton can acceptt a varying amont of arguments

# Say you want to add more than just two numbers - the below code will not work if un-commented:
# def add(num1, num2):
#    sum = num1 + num2
#    return sum

# print(add(1,2,3))

def add(*stuff):
    sum = 0  # initializes a variable 'sum' to 0
    stuff = list(stuff)  # converts the typle of arguments ('stuff') tot a list. So we can edit the list below
    stuff.append(10)  # adds 10 to the end of the list
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
