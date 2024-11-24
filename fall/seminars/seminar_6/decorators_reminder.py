def uppercase(func):
    def wrapper():
        func_result = func()
        return func_result.upper()

    return wrapper


# def greet():
#     return "Hello"

# decorated_hello = uppercase(greet)


@uppercase
def greet():
    return "Hello"

print(greet())
