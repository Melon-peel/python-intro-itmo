from functools import wraps


def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """doc string for wrapper"""
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_something(something):
    """some doc string"""
    return f"I said {something}"

print(say_something.__doc__)
# print(say_something("Patrick"))
# print(say_something.__wrapped__("Patrick"))

#print(say_something("Patrick"))
#print(say_something.__wrapped__("Patrick"))
# print(say_something("Patrick"))
