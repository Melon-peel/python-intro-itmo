class Car:
    def __init__(self, brand, doors_num):
        self.__brand = brand
        self.__doors_num = doors_num

    def get_brand(self):
        return self.__brand

    def set_brand(self, b):
        self.__brand = b

    def get_doors(self):
        return self.__doors_num

    def set_doors(self, d):
        self.__doors = d

    def info(self):
        return "Nice car with " + str(self.__doors_num) + " doors"


class Truck(Car):

    def __init__(self, brand, doors_num, load_weight, axes):
        super().__init__(brand, doors_num)
        self.__load_weight = load_weight
        self.__axes = axes

    def info(self):
        return "Nice truck with " + str(self.get_doors()) + " doors"


class Limousine(Car):

    def __init__(self, brand, doors_num, has_glass_roof):
        super().__init__(brand, doors_num)
        self.__glass_roof = "with" if has_glass_roof else "without"

    def info(self):
        return f"Nice limo {self.__glass_roof} a glass roof"

# ---------------------
# Polymorphism via inheritance
# ---------------------
cars = [Truck(1, 4, 5, 6),
        Limousine(1, 4, True)]
for car in cars:
    print(car.info())
