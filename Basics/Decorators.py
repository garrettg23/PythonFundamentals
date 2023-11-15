#  A decorator is a special type of function that can be used to modify the behavior of another function. Decorators
#  are often used to wrap or modify the functionality of functions or methods. They are applied using the @decorator
#  syntax above the function definition.

# note the decorator @log_function_call takes in one argument, in this case takes in the add function and
# multiply function defined beneath.

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} execution completed")
        return result
    return wrapper


@log_function_call
def add(a, b):
    return a + b


@log_function_call
def multiply(a, b):
    return a * b


result_add = add(3, 5)
result_multiply = multiply(4, 6)
result2_add = add(19, 20)

print(result_add)
print(result_multiply)
print(result2_add)
