# tuple = collection which is ordered and unchangeable, used to group together related data

student = ("Garrett",26,"Male","Kyle",27,"Male","Garrett",34,"Male")

# Count of objects in tuple equal to Garrett
print(student.count("Garrett"))

# Prints the index where the value Male first appears.
print(student.index("Male"))

# print out the tuple
for x in student:
    print(x)

# roll call
if "Garrettt" in student:
    print("Garrett is here!")