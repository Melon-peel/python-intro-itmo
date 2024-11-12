class Car:
    _doors_number = 5

    def __init__(self, custom_color, model):
        self.custom_color = custom_color
        self._model = model
        self.__model_code = None

    def _decorate_model(self):
        return self._model.upper()

    def get_model(self):
        return self._decorate_model()

    def set_model_code(self, model_code):
        self.__model_code = model_code

    def get_model_code(self):
        return self.__model_code

    def _move(self):
        pass

audi = Car("green", "tt")
print(audi._Car__model_code)

