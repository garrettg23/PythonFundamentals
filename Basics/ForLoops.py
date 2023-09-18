import time

# for loop = a statement that will execute it's block of code a limited amount of times.
#
# while loop = unlimited
# for loop = limited

# this prints 1 through 10
for i in range(10):
    print(i+1)

# count between two numbers, first number inclusive, last number exclusive
# do this prints 50 through 99
for i in range(50,100):
    print(i)

# you can add a step value in the range, count up by 2 example
for i in range(1,10,2):
    print(i+1)

# Lets make a for loop for a countdown from 10, one digit a second.
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
