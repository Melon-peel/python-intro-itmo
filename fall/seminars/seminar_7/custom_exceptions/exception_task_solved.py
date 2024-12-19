# Необходимо создать два класса для обработки исключений

# Первый класс - InvalidValueError - предназначен для обработки случаев, когда
# передано отрицательное число

class InvalidValueError(Exception):

    # внутри конструктора:
    # объекту присваиваются message и value
    def __init__(self, value, message="Invalid value provided"):
        self.value = value
        self.message = message

    # возвращается строка в формате "self.message: self.value"
    def __str__(self):
        return f"{self.message}: {self.value}"



# Второй класс - OperationNotAllowedError - сигнализирует о попытке выполнить запрещённую операцию
# пусть такой операцией будет деление на ноль

class OperationNotAllowedError(Exception):

    def __init__(self, message="Operation not allowed"):
        self.message = message

    def __str__(self):
        return self.message
    # Operation not allowed
    # то же самое, но без передачи value в конструктор
    # __str__ будет возвращать просто "self.message"



class Calculator:


    @staticmethod
    def add(left, right):
        # сложение двух чисел и проверка на то, что каждое из них - положительное
        # иначе вызов InvalidValueError
        if (min_val := min(left, right)) < 0:
            raise InvalidValueError(min_val)
        else:
            return left + right

    @staticmethod
    def divide(left, right):
        # деление двух чисел и проверка на то, что правое не ноль
        # иначе вызов OperationNotAllowedError
        if right == 0:
            raise OperationNotAllowedError()
        else:
            return left / right
calc = Calculator()

# попробуйте:
# 1. сложить 1 и 5
# 2. сложить -10 и 2
# 3. разделить 10 на -10
# 4. разделить 1 на 0
