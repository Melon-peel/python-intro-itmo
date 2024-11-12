def uppercase(func):
    def wrapper():
        func_result = func()
        return func_result.upper()
    return wrapper

def greet():
    return "Hello"

decorated_greet = uppercase(greet)

@uppercase
def greet():
    return "Hello"


