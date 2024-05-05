# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def MidGray(img):
    img = np.array(img)
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    gris = (0.299*R + 0.587*G + 0.114*B)
    return gris

def imagenBinarizar(imagen, umbral):
    imagen = np.array(imagen) / 255
    imagen = MidGray(imagen)
    imagenBin = imagen>= umbral * 0.255
    return imagenBin
    


imagen = plt.imread('SP.jpg')

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Original')
plt.axis('off')

imagen_ajustada = imagenBinarizar(imagen, 1.5)

# Mostrar la imagen con brillo ajustado
plt.subplot(1, 2, 2)
plt.imshow(imagen_ajustada)
plt.title('Binarizacion ajustada')
plt.axis('off')

plt.show()
