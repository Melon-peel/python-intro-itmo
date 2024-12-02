def division(a, b):
    return a / b

try:
    print(division(1, "dfsd"))
except Exception as e:
    print(e)
    raise
    # raise TypeError("Ошибка типа")  # raise TypeError()
