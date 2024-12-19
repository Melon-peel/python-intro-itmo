# Необходимо создать два класса для обработки исключений

# Первый класс - InvalidValueError - предназначен для обработки случаев, когда
# передано отрицательное число

class InvalidValueError(Exception):

    # внутри конструктора:
    # объекту присваиваются message и value
    def __init__(self, value, message="Invalid value provided"):
        ...

    # возвращается строка в формате "self.message: self.value"
    def __str__(self):
        ...


# Второй класс - OperationNotAllowedError - сигнализирует о попытке выполнить запрещённую операцию
# пусть такой операцией будет деление на ноль

class OperationNotAllowedError(Exception):

    # то же самое, но без передачи value в конструктор
    # message по умолчанию "Operation not allowed"
    # __str__ будет возвращать просто "self.message"
    ...



class Calculator:

    @staticmethod
    def add(left, right):
        # сложение двух чисел и проверка на то, что каждое из них - положительное
        # иначе вызов InvalidValueError
        ...

    @ staticmethod
    def divide(left, right):
        # деление двух чисел и проверка на то, что правое не ноль
        # иначе вызов OperationNotAllowedError
        ...

# попробуйте:
# 1. сложить 1 и 5
# 2. сложить -10 и 2
# 3. разделить 10 на -10
# 4. разделить 1 на 0
