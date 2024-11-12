class Car:
    doors_number = 5

    def __init__(self, color, model):
        self.custom_color = color
        self.model = model
        self.doors_number = 10


def f():
    doors_number = 5

audi = Car(color="green", model="TT")
print(audi.__class__.doors_number)


