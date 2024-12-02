def division(a, b):
    return a / b

a, b = 1, 0
try:
    # Код, который может вызвать исключение
    result = division(a, b)
except Exception as e:
    # Код для обработки любого исключения, которое наследуется от Exception, и получения
    # доступа к атрибутам исключения через переменную e
    print(f"Error occurred: {e}")
else:
    # Код, который запустится, если исключение не возникло
    print(f"Division result is {result}")
finally:
    # Код, который запустится в любом случае
    print(f"Division {a}/{b} was attempted")