from PIL import Image
import os


class JPEGCompressor:
    def __init__(self):
        ...

    def load(self, filepath):
        # os.path.exists(filepath) может быть использован для проверки на наличие файла
        # Image.open(filepath) может быть использована для создания объекта Image
        ...

    def compress(self, quality):
        ...

    def save(self, filepath):
        # сохранение изображения выглядит следующим образом
        # Image.save(filepath, format=..., quality=..., optimize=True)
        # format - нужный формат
        # quality - выбранное качество
        # флаг optimize оставьте в True (если интересно -> Ctrl+F "Optimize" https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)
        ...

# код ниже должен работать, если вы сделали всё верно
compressor = JPEGCompressor()
compressor.load("wallpapers.jpeg")
compressor.compress(10)
compressor.save("wallpapers_compressed.jpeg")

