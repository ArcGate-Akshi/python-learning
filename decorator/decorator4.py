# decorator with arguments
from functools import wraps


def allowed_data_type(data_type):
    def decor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("invalid data")
        return wrapper
    return decor


@allowed_data_type(str)
def string(*args):
    strings = ''
    for i in args:
        strings += i
    return strings


print(string('akshi', 'modi', 'jain',))


@allowed_data_type(int)
def integ(*args):
    total = 0
    for i in args:
        total += i
    return total


print(integ(1, 5, 7, 8))
