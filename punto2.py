# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def ajustar_brillo_canal(imagen, canal, factor):
    imagen = np.array(imagen) / 255
    imagen[:,:,canal] = imagen[:,:,canal]*factor
    
    return imagen

imagen = plt.imread('SP.jpg')

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Original')
plt.axis('off')

imagen_ajustada = ajustar_brillo_canal(imagen, 2 , 10)

# Mostrar la imagen con brillo ajustado
plt.subplot(1, 2, 2)
plt.imshow(imagen_ajustada)
plt.title('Brillo canal ajustado')
plt.axis('off')

plt.show()
