import PIL 
from PIL import Image
import matplotlib.pyplot as plt

imagen = Image.new("RGB",(50,50), (33,74,86))

imagen.save("cuadrado.png")

plt.imshow(imagen)
plt.axis("off")
plt.show()
