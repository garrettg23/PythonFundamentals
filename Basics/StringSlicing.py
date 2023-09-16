# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step] or (start,stop,step)

# indexing section
name = "Garrett Galarneau"

first_name = name[0:7] # indexing, note the stop is exclusive.
# you can also do this and it starts at the beginning of the string.
first_name = name[:7]

last_name = name[8:17]
# You can also do this to end at the end of a string
last_name = name[8:]

step_example = name[::2] # Every other character prints, from start to end

reverse_name = name[::-1] # Reverse name, backwards step

print(first_name)
print(last_name)
print(step_example)
print(reverse_name)

# slice section
website1 = "http://youtube.com"
website2 = "http://google.com"

web_slice = slice(7,-4) # slices all websites the same, returns just site name.

print(website1[web_slice])
print(website2[web_slice])
