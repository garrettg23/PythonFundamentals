# similar to ReadFile.py, there is a mode / second argugment you can pass in
# see comma after path, usually set to 'r' for read by default.
# the below will overwrite the file if it exists as well.
text ="Hello!\nThe forward slash n creates a new line. \nCheck out this new .txt file! You a bitch"

with open("C:\Documents\PythonOsTraining\Test2.txt",'w') as file:
    file.write(text)

# Read the new file.
with open("C:\Documents\PythonOsTraining\Test2.txt") as file:
    print(file.read())
