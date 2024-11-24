import random


# Класс для работы с датчиком температуры
class TemperatureSensor:

    # должен быть аргумент `sensor_name`, имеющий значений "Temperature Sensor" по умолчанию
    # данный аргумент становится атрибутом self.sensor_name
    def __init__(self, sensor_name="Temperature Sensor"):
        self.sensor_name = sensor_name

    # здесь должен быть статический метод read_temperature()
    @staticmethod
    def read_temperature():
        return round(random.uniform(15, 30), 2)
    # данный метод вызывает random.uniform(15, 30) для симуляции считывания температуры
    # после чего полученное значение округляется до двух знаков после запятой и возвращается
    # your code here



# Здесь должен быть класс LightController с методами:
# __init__, не принимающим аргументов, но задающим атрибут self.light_on = False
# toggle_light, являющимся методом объекта со следующей логикой
#     1) при вызове метода он переключает свет (т.е. меняет self.light_on на обратное значение)
#     2) печатает через print строку "Освещение сейчас: state", где state - строка, равная "включено", если
#                                                               self.light_on == True, а иначе - "выключено"
class LightController:

    def __init__(self):
        self.light_on = False

    def toggle_light(self):
        self.light_on = not self.light_on
        state = "включено" if self.light_on else "выключено"
        print(f"Освещение сейчас: {state}")

# Здесь должен быть класс SmartDevice, наследующий классы TemperatureSensor и LightController
# данный класс должен иметь только конструктор, совместимый с родителями - т.е. принимающий аргумент sensor_name
# внутри конструктора вызываются конструкторы родителей
# например, конструктор класса LightController - LightController.__init__
class SmartDevice(TemperatureSensor, LightController):
    def __init__(self, sensor_name="Temperature Sensor"):
        TemperatureSensor.__init__(self, sensor_name)
        LightController.__init__(self)

