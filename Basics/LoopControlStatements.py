# Loop Control Statements = changa a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips the next iteration of the loop.
# pass = does nothing, acts as a placeholder

# Break example, using ask for a name:
while True:
    name = input("Enter your name: ")
    if name !="":
        break

print(name)

# Continue example, print phone number without "-"'s:
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print("") # this is to allow the next look to run properly, without adding to phone number


# Pass example, print 1-20 in a for loop, but skip 13:
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

# note that the above example of pass acts as a continue, but "else:" is needed.
