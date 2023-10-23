# dictionary = A changeable, unordered collection of unique key:value pairs
# fast because they use hashing, allow us to access a vlue quickly.

capitals = {'USA':'Washington DC',
           'India':'New Dehli',
           'China':'Beijing'}

# prints value from the key. Breaks if key does not exist.
print(capitals['USA'])

# better way to find the value for a key is get method.
print(capitals.get('USA'))

# add berlin, germany to capitals
capitals.update({'Germany':'Berlin'})
# update a pair, USA's capital is now new world order town.
capitals.update({'USA':'New World Order Town'})
# Removes the key value pair based off the key
capitals.pop('China')


print("The index in a dictionary prints the keys:")

for i in capitals:
    print(i)
print()

print("This also prints the keys:")

for key in capitals.keys():
    print(key)
print()

print("This prints the values:")

for value in capitals.values():
    print(value)
print()

print("This will print the key value pairs as a list of tuples:")
for item in capitals.items():
    print(item)
print()

print("The below is another way to print the items, keys, or values:")
print(capitals.items())
print(capitals.keys())
print(capitals.values())
print()

# clears the entire dict
capitals.clear()
print(capitals.items())
