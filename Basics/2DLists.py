# 2D lists = a list of lists

drinks = ["cofee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks,dinner,dessert]

# prints the 2d list
print(food)

# prints first index of 2d list, ie. the drinks list
print(food[0])

# prints the first item within the first list of 2 d lists
print(food[0][1])

# adding sample space here between this and the nested for loop
print("")

# prints each item individually of a 2d list
for i in food:
    for item in i:
        print(item)
