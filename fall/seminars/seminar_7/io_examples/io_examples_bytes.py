import io
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image


simple_plot = plt.scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4])
buffer = io.BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)

im = Image.open(buffer)
im.show()
buffer.close()