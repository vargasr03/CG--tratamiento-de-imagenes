# Taller 4
# Valentina Vargas Rudas
# Código 1006466282
# Universidad Tecnológica de Pereira

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage import exposure
from skimage.color import rgb2gray

#lee la imagen del archivo, va a ser la imagen principal usada
imagen = io.imread("real.jpg")/255.0

#1
#Procedimiento para crear la imagen mostrada en el taller
"""
    Se crea una matriz con las dimensiones deseadas, luego a cada submatriz de la imagen se
    le asigna el color deseado
"""
def primer_punto():
    A = np.zeros((402,402,3))
    A[0:135,0:135] = np.array((0,255,255)) / 255.0
    A[0:135,135:269] = np.array((255,255,255)) / 255.0
    A[0:135,269:403] = np.array((255,0,0)) / 255.0
    A[135:269,0:135] = np.array((255,0,255)) / 255.0
    A[135:269,135:269] = np.array((128,128,128)) / 255.0
    A[135:269,269:403] = np.array((0,255,0)) / 255.0
    A[269:403,0:135] = np.array((255,255,0)) / 255.0
    A[269:403,135:269] = np.array((0,0,0)) / 255.0
    A[269:403,269:403] = np.array((0,0,255)) / 255.0
    plt.imshow(A)


#2
#Procedimiento muy parecido al anterior
def segundo_punto():
    matriz_rgb = np.random.randint(0, 256, (8, 12, 3))
    matriz_rgb[:6,:2,:] = [255,255,0]
    matriz_rgb[:6,2:4,:] = [0,255,255]
    matriz_rgb[:6,4:6,:] = [0,255,0]
    matriz_rgb[:6,6:8,:] = [255,0,255]
    matriz_rgb[:6,8:10,:] = [255,0,0]
    matriz_rgb[:6,10:12,:] = [0,0,255]

    matriz_rgb[6:8,0,:] = [255,255,255]
    matriz_rgb[6:8,1,:] = [240,240,240]
    matriz_rgb[6:8,2,:] = [220,220,220]
    matriz_rgb[6:8,3,:] = [200,200,200]
    matriz_rgb[6:8,4,:] = [175,175,175]
    matriz_rgb[6:8,5,:] = [150,150,150]
    matriz_rgb[6:8,6,:] = [125,125,125]
    matriz_rgb[6:8,7,:] = [100,100,100]
    matriz_rgb[6:8,8,:] = [75,75,75]
    matriz_rgb[6:8,9,:] = [50,50,50]
    matriz_rgb[6:8,10,:] = [25,25,25]
    matriz_rgb[6:8,11,:] = [0,0,0]

    matriz_rgb = matriz_rgb / 255.0

#3
"""
    Nombre del proceso: invertir_colores()
    objetivo: invertir los colores de la imagen principal "linea 8"
    retorna: void
"""
def invertir_colores():
    imagen_invertida = 1 - imagen
    plt.imshow(imagen_invertida)


#muestra en pantalla las funciones 4, 5 y 6
def capas():
    plt.subplot(221)
    plt.imshow(capa_roja())
    plt.subplot(222)
    plt.imshow(capa_verde())
    plt.subplot(223)
    plt.imshow(capa_azul())

#4
"""
    Nombre del proceso: capa_roja()
    objetivo: retornar la capa roja de la imagen principal "linea 8"
    retorna: imagen_roja
"""
def capa_roja():
    imagen_roja = np.copy(imagen)
    imagen_roja[:,:,1] = 0
    imagen_roja[:,:,2] = 0
    return imagen_roja

#5
"""
    Nombre del proceso: capa_verde()
    objetivo: retornar la capa verde de la imagen principal "linea 8"
    retorna: imagen_verde
"""
def capa_verde():
    imagen_verde = np.copy(imagen)
    imagen_verde[:,:,0] = 0
    imagen_verde[:,:,2] = 0
    return imagen_verde

#6
"""
    Nombre del proceso: capa_azul()
    objetivo: retornar la capa azul de la imagen principal "linea 8"
    retorna: imagen_azul
"""
def capa_azul():
    imagen_azul = np.copy(imagen)
    imagen_azul[:,:,0] = 0
    imagen_azul[:,:,1] = 0
    return imagen_azul

#muestra en pantalla las funciones 7, 8 y 9
def colores():
    plt.subplot(221)
    plt.imshow(magenta())
    plt.subplot(222)
    plt.imshow(cian())
    plt.subplot(223)
    plt.imshow(amarillo())

#7
"""
    Nombre del proceso: magenta()
    objetivo: retornar la capa magenta de la imagen principal "linea 8"
    retorna: imagen_magenta
"""
def magenta():
    filas = imagen.shape[0]
    columnas = imagen.shape[1]
    imagen_magenta = np.copy(imagen)
    imagen_magenta[:,:,0] = np.ones((filas,columnas))*255
    imagen_magenta[:,:,2] = np.ones((filas,columnas))*255
    return imagen_magenta

#8
"""
    Nombre del proceso: cian()
    objetivo: retornar la capa cian de la imagen principal "linea 8"
    retorna: imagen_cian
"""
def cian():
    filas = imagen.shape[0]
    columnas = imagen.shape[1]
    imagen_cian = np.copy(imagen)
    imagen_cian[:,:,1] = np.ones((filas,columnas))* 255
    imagen_cian[:,:,2] = np.ones((filas,columnas))* 255
    return imagen_cian

#9
"""
    Nombre del proceso: amarillo()
    objetivo: retornar la capa amarillo de la imagen principal "linea 8"
    retorna: imagen_amarillo
"""
def amarillo():
    filas = imagen.shape[0]
    columnas = imagen.shape[1]
    imagen_amarillo = np.copy(imagen)
    imagen_amarillo[:,:,0] = np.ones((filas,columnas))* 255
    imagen_amarillo[:,:,1] = np.ones((filas,columnas))* 255
    return imagen_amarillo

#10
"""
    Nombre del proceso: reconstruir_capas(capa_roja,capa_verde,capa_azul)
    parametros: capa_roja: capa roja de una imagen, capa_verde: capa verde de una imagen,
                capa_azul: capa azul de una imagen,
    objetivo: reconstruir una imagen dadas las 3 capas separadas de la misma
    retorna: void
"""
def reconstruir_capas(capa_roja,capa_verde,capa_azul):
    imagen_reconstruida = capa_roja+capa_verde+capa_azul
    plt.imshow(imagen_reconstruida)


#11
"""
    Nombre del proceso: fusion_sin_ec(imagen1,imagen2)
    parametros: imagen1, imagen2 : imagenes a fusionar
    objetivo: fusionar 2 imagenes sin ecualizar
    retorna: imagen_fusionada
"""
def fusion_sin_ec(imagen1,imagen2):
    imagen_fusionada = np.maximum(imagen1, imagen2)
    return imagen_fusionada

#12
"""
    Nombre del proceso: fusionar_y_ecualizar(imagen1,imagen2)
    parametros: imagen1, imagen2 : imagenes a fusionar
    objetivo: fusionar 2 imagenes y las ecualiza
    retorna: funsion_ecualizada
"""
def fusionar_y_ecualizar(imagen1, imagen2):
    fusion = imagen1 + imagen2
    fusion_ecualizada = exposure.equalize_hist(fusion)
    return fusion_ecualizada

#13
"""
    Nombre del proceso: ecualizar_con_factor(imagen,factor)
    parametros: imagen: imagen a ecualizar, factor: factor a ecualizar la imagen
    objetivo: ecualizar una imagen con un factor dado
    retorna: imagen_ecualizada
"""
def ecualizar_con_factor(imagen, factor):
    imagen_ecualizada = exposure.adjust_gamma(imagen, gamma=factor)
    return imagen_ecualizada

#14
def average(image):
    # Definimos la máscara del filtro de promedio (3x3)
    mask = np.ones((3,3))/9
    
    # Aplicamos el filtro a la imagen utilizando la función convolve de NumPy
    imagen_average = np.zeros_like(image)
    for i in range(3):
        imagen_average[:,:,i] = np.convolve(image[:,:,i].flatten(), mask.flatten(), mode='same').reshape(image.shape[:2])
    
    return imagen_average

#15
def average_gris(imagen):
    # Sumar las componentes RGB y dividir entre 3 para obtener el promedio
    R = imagen[:,:,0]
    G = imagen[:,:,1]
    B = imagen[:,:,2]
    imagen_gris = (R + G + B)/3
    return imagen_gris

#16
def luminosity(imagen):
    imagen_gris = np.dot(imagen[:,:,:3], [0.299, 0.587, 0.114])
    return imagen_gris

#17
def midgray(imagen):
    imagen_gris = np.copy(imagen)
    imagen_gris = (np.max(imagen,axis=2)+np.min(imagen,axis=2))/2
    return imagen_gris

primer_punto()
plt.show()
segundo_punto()
plt.show()
invertir_colores()
plt.show()
capas()
plt.show()
colores()
plt.show()
reconstruir_capas(capa_roja(),capa_verde(),capa_azul())
plt.show()
imagen1 = io.imread("paisaje.jpg")/255.0
imagen2 = io.imread("perro.jpeg")/255.0
plt.imshow(fusion_sin_ec(imagen1,imagen2))
plt.show()
plt.imshow(fusionar_y_ecualizar(imagen1,imagen2))
plt.show()
plt.imshow(ecualizar_con_factor(imagen1,3))
plt.show()
plt.imshow(average(imagen1))
plt.show()
plt.rcParams["image.cmap"] = "gray"
plt.subplot(221)
plt.imshow(average_gris(imagen1))
plt.subplot(222)
plt.imshow(luminosity(imagen1))
plt.subplot(223)
plt.imshow(midgray(imagen1))
plt.show()
