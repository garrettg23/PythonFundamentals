# sort() method = used with lists
# sort() function = used with iterables

# only works with [lists] not (tuples)
studentsList = ["Bob","Alice","Tiffany","John"]

studentsList.sort()

for i in studentsList:
    print(i)

# reverse
studentsList.sort(reverse=True)

for i in studentsList:
    print(i)

# how to use function for tuples
studentsTuple = ["Bob","Alice","Tiffany","John"]

sorted_students = sorted(studentsTuple, reverse=True)

for i in sorted_students:
    print(i)

# how to use with list of tuples. name, grade, age
studentsListTuple = [("Bob", "A", 41),
                     ("Alice", "D", 23),
                     ("Tiffany", "C", 51),
                     ("John", "B", 59)]

# sort on first index of tuple
studentsListTuple.sort()

for i in studentsListTuple:
    print(i)

# sort on grades
grade = lambda grades:grades[1]
studentsListTuple.sort(key=grade)

for i in studentsListTuple:
    print(i)

# need to add tuple of tuple example here
