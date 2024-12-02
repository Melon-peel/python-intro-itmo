def division(a, b):
    return a / b

try:
    # Код, который может вызвать исключение
    division(1, "fff")
except NotImplementedError:
    # Код для обработки исключения NotImplementedError
    ...
except Exception as e:
    # Код для обработки любого исключения, которое наследуется от Exception, и получения доступа
    # к атрибутам исключения через переменную e (в частности - к информации о природе ошибки)
    print(e)
    print("Exception caught")
except (ZeroDivisionError, ValueError):
    # Код для обработки хотя бы одного из исключений выше
    ...
except (ZeroDivisionError, TypeError) as e:
    # Код для обработки хотя бы одного из исключений выше и получения доступа
    # к атрибутам исключения через переменную e
    print(f"Произошла ошибка {type(e)}: {e}")
except:
    # Код для обработки любого исключения
    # Ещё можно except Exception (... as e)
    print("Exception occurred")

