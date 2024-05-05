# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def ajustar_contraste(imagen, factor):
    imagen = np.array(imagen) / 255
    imagen_ajustada = factor * np.log10(1 + imagen)
    
    return imagen_ajustada

imagen = plt.imread('SP.jpg')

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Original')
plt.axis('off')

imagen_ajustada = ajustar_contraste(imagen, 5)

# Mostrar la imagen con brillo ajustado
plt.subplot(1, 2, 2)
plt.imshow(imagen_ajustada)
plt.title('Contraste ajustado')
plt.axis('off')

plt.show()
