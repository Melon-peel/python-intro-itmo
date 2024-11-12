class Car:
    doors_number = 5
    instance_count = 0

    def __init__(self, brand, production_year):
        self.brand = brand
        self.production_year = production_year

    @classmethod
    def create_default_car(cls):
        # To create a default instance
        return cls(brand=None, production_year=2024)

    @classmethod
    def get_instance_count(cls):
        # to access class attr
        return cls.instance_count

    @classmethod
    def set_doors_number(cls, doors):
        # To change some aspects of the class
        cls.doors_number = doors

    @staticmethod
    def is_warranty_active(production_year):
        return production_year < 2030

    def info(self):
        print("Car: " + self.brand)
        print("Production year: " + str(self.production_year))
        if self.is_warranty_active(self.production_year):
            print("Warranty is ACTIVE")
        else:
            print("Warranty is NOT active")



# print(audi.brand)
# audi.info()
# print(audi.brand)

