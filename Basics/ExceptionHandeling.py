# exception = events detectected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Big dumb dumb.")
except ValueError as e:
    print(e)
    print("Enter only numbers please...")
except Exception as e:
    print(e)
    print("something went wrong: (")
else:
    print(f"The numerator divided by your denominator is {result}")
finally:
    print("Run again if you want!")
