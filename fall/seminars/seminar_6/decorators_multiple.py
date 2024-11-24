# украдено отсюда https://habr.com/ru/companies/otus/articles/727590/

def boldize(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italicize(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

@boldize
@italicize
def greet():
    return "Hello!"

print(greet())
# decorated_greet = strong(emphasis(greet))

