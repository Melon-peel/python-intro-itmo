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
        self.__doors_num = d

    def info(self):
        return "Nice car with " + str(self.__doors_num) + " doors"


class Truck(Car):

    def __init__(self, brand, doors_num, load_weight, axes):
        super().__init__(brand, doors_num)
        self.__load_weight = load_weight
        self.__axes = axes

    def get_brand(self):
        return self.__brand

    def get_load(self):
        return self.__load_weight

    def set_load(self, l):
        self.__load_weight = l

    def get_axes(self):
        return self.__axes

    def set_axes(self, a):
        self.__axes = a

my_truck = Truck(1, 2, 3, 4)
my_truck.get_brand()
