#decorator
from functools import wraps


def print_func_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"you are calling {func.__name__} function")
        print(f"{func.__doc__}")
        return func(*args, **kwargs)
    return wrapper


@print_func_data
def add(a, b):
    '''this function takes two numbers as arguments and return their sum'''
    return a+b


print(add(4, 5))
