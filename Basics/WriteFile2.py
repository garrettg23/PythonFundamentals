import os
# This is an extension of WriteFile.py
# This will check if the file exists, before writing it.
# If it exists it will ask the user if they want to overwrite.
# If it does not exist it will write the new file.

file_path = "C:\Documents\PythonOsTraining\Test3.txt"
text_input = "This will insert to new file \nnew line if you need it"

def write_read_file(file, text):
    with open(file_path, 'w') as file:
        file.write(text_input)
    print("Here is what your new or overwritten file contains: ")
    with open(file_path) as file:
        print(file.read())

if os.path.isfile(file_path) == False:
    print("The path input did not exist before, writing a new file to that path.")
    write_read_file(file_path,text_input)
else:
    print("That file already exists, do you want to overwrite it?")
    check = input("Please input Y/N here: ")
    if check == "Y":
        write_read_file(file_path,text_input)
    elif check == "N":
        print("Okay, the file will remain as is.")
    else:
        print("Y or N was not input, please re-run.")
