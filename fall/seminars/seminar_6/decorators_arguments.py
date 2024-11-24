def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_something(something):
    return f"I said {something}"

print(say_something("Patrick"))
