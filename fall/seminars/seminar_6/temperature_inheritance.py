import random

# Класс для работы с датчиком температуры
class TemperatureSensor:
    def __init__(self, sensor_name="Temperature Sensor"):
        self.sensor_name = sensor_name

    @staticmethod
    def read_temperature():
        # как-то считывает температуру
        temperature = random.uniform(15, 30)
        return round(temperature, 2)

# Класс для управления освещением
class LightController:
    def __init__(self):
        self.light_on = False

    def toggle_light(self):
        self.light_on = not self.light_on
        state = "включено" if self.light_on else "выключено"
        print(f"Освещение сейчас: {state}")


# Класс, объединяющий функционал двух предыдущих
class SmartDevice(TemperatureSensor, LightController):
    def __init__(self, sensor_name="Smart Device"):
        TemperatureSensor.__init__(self, sensor_name)
        LightController.__init__(self)



