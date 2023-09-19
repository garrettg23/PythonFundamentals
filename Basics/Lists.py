# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

# replaces first value / index in food variable
food[0] = "sushi"

# add to list:
food.append("ice cream")

#remove from a list:
food.remove("hotdog")

#removes the last element from list, removes ice cream from above
food.pop()

#insert into list at certain index. This replaces pizza at the front
food.insert(0,"pizza")

#sort list alphabetically
food.sort()

#to clear this list you can do: food.clear()

print(food)
print(food[3])

list_length = len(food)
print(list_length)

#simple print of items in a list
for i in food:
    print(i)

# print the list as a comma separated string using a for loop and enumerate
for i, item in enumerate(food):
   if i == list_length -1:
       print(item)
   else:
       print(item + ", ", end="")
