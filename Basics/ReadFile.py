# reads file, closes it after automatically (with open does this)
# try block to catch incorrect file name / path.
try:
    with open("C:\Documents\PythonOsTraining\Test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
