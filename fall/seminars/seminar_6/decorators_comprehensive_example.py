import time
import logging
from functools import wraps

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)


# Декоратор для логирования вызовов функции
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' called with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


# Декоратор для ограничения времени выполнения функции
def timeout(max_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > max_seconds:
                raise TimeoutError
            return result

        return wrapper

    return decorator



# Пример использования двух декораторов


@log_calls
@timeout(max_seconds=2)
def compute_square_sum(n):
    time.sleep(1)  # Симуляция долгой работы
    return sum(i ** 2 for i in range(n))

print(10_000_000_000.1_23_45)

#
# try:
#     print(compute_square_sum(10))  # Функция успеет выполниться
#     print(compute_square_sum(10_000_000))  # Функция превысит лимит времени
# except TimeoutError as e:
#     logging.error(e)
