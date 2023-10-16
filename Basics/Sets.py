# set = collectiton which is unordered, unindexed. No duplicate values.

utensils = {"fork","knife","spoon"}
dishes = {"bowl","plate","cup","knife"}

# adds item to set
utensils.add("napkin")
print(utensils)

# removes item from set
utensils.remove("napkin")
print(utensils)

# sets new set to be all of the unique items from these two sets
dinner_table=dishes.union(utensils)
print(dinner_table)

# You can also do something similar to a union by updating a set with another set.
dishes.add("spatula")
dinner_table.update(dishes)
print(dinner_table)

# compare elements between sets and or in common (diff vs intersect)
utensils.add("spork")
print(utensils.difference(dinner_table))
print(utensils.intersection(dinner_table))

# clear all the items in a set
utensils.clear()
print(utensils)
