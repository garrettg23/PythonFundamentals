# **kwargs= paramter that will pack all arguments in to a dictionary
# useful so that a function can accept a varying amount of keyword arguments.

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(str(value), end=" ")


hello(first="Joe", last="Shmoe", age=21)
