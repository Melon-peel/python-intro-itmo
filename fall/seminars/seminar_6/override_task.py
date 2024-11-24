import math

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("Операнд должен быть объектом Vector2D")
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("Операнд должен быть объектом Vector2D")
        return Vector2D(self.x - other.x, self.y - other.y)


    def __mul__(self, other):
        if isinstance(other, Vector2D):
            # Скалярное произведение
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            # Умножение на число
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError("Операнд должен быть числом или объектом Vector2D")

    def __abs__(self) -> float:
        # Длина вектора
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

# Пример использования
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
