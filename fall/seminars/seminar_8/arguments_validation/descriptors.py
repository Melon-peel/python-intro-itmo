class MyDescriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called: instance={instance}, owner={owner}")
        return self.value

    def __set__(self, instance, value):
        print(f"__set__ called: instance={instance}, value={value}")
        self.value = value

class Citizen:
    age = MyDescriptor()

    def __init__(self, attr_arg):
        self.age = attr_arg


my_obj = Citizen(10)
print(my_obj.age)
