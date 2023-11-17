import random

x = random.randint(1, 6)  # dice roll
y = random.random()  # random float point number between 0 (inclusive) and 1 (exclusive)

myList = ['Rock', 'Paper', 'Scissors']
z = random.choice(myList)  # random choice of list

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)  # shuffle cards

print(x)
print(y)
print(z)

for i in cards:
    print(i, end=" ")
