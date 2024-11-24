class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        elif isinstance(other, Vector2D):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError

    def __str__(self):
        return f"({self.x}, {self.y})"

vector_1 = Vector2D(2, 3)
vector_2 = Vector2D(10, -1)
print(vector_1 * vector_1)