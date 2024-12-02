def division(a, b):
    return a / b


try:
    print(division(1, 2))
    a = [1, 2, ]
    a[10]
except ZeroDivisionError:
    print("Can't divide by 0!")
except TypeError:
    print("Division only supports number division!")
