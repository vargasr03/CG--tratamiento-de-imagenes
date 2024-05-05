# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def histograma_capas(imagen):
    alto, ancho, canales = imagen.shape

    fig, axs = plt.subplots(canales, figsize=(10, 6))

    for canal in range(canales):
        valores = imagen[:, :, canal].ravel()

        histograma, bordes = np.histogram(valores, bins=256, range=(0, 256))

        axs[canal].plot(histograma, color='black')
        axs[canal].set_title(f'Capa {canal + 1}')
        axs[canal].set_xlim([0, 256])

    plt.tight_layout()
    plt.show()

# Ejemplo de uso
imagen = plt.imread('SP.jpg') 
histograma_capas(imagen)
