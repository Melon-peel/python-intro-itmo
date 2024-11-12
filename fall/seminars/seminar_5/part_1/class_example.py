class Car:
    """
    Some docstring
    """

    doors_number = 5

    def __init__(self, color, model):
        self.color = color
        self.model = model


audi = Car("green", "TT")
mercedes = Car(color='metalic', model='Benz')

# print(audi.__class__.__dict__)
# print(Car.__dict__)

print(dir(audi))

# class Car:
#     doors_number = 5
#
#     def __init__(self, color, model):
#         self.custom_color = color
#         self.model = model
#         self.doors_number = 10
#
#
#
# audi = Car(color="green", model="TT")
#
# # print(Car.__dict__)
# # print(audi.__dict__)

