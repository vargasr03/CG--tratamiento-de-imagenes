# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def imagenZoom(imagen, zoom, pinicial):
    imagen = imagen / 255
    filas = imagen.shape[0]
    columnas = imagen.shape[1]

    pinicial_i = pinicial[0]
    pinicial_j = pinicial[1]

    beta = zoom
    imagenz = np.copy(imagen)

    for i in range(filas):
        for j in range(columnas):
            # Calcula los índices en la imagen original a partir de los índices en la imagen zoom
            i_original = int(pinicial_i + i / zoom)
            j_original = int(pinicial_j + j / beta)

            # Asegura que los índices estén dentro de los límites de la imagen original
            i_original = min(max(i_original, 0), filas - 1)
            j_original = min(max(j_original, 0), columnas - 1)

            imagenz[i, j] = imagen[i_original, j_original]

    return imagenz


imagen = plt.imread('SP.jpg')

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Original')
plt.axis('off')

imagen_ajustada = imagenZoom(imagen, 5, (500,0))

# Mostrar la imagen con brillo ajustado
plt.subplot(1, 2, 2)
plt.imshow(imagen_ajustada)
plt.title('Zoom ajustado')
plt.axis('off')

plt.show()
