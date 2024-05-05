# Valentina Vargas - Juan Chaux

import numpy as np
import matplotlib.pyplot as plt

def inv(img):
    img = np.array(img)
    return(255 - img)

def rotarImagen(miImagen, angulo):
    # Importo la imagen a trabajar
    Imagen = (miImagen)/255
    angulo = angulo* np.pi/180
    h,w,c =np.shape(Imagen)
    mat_inv= inv(np.array([[np.cos(angulo),np.sin(angulo),0],[-np.sin(angulo),np.cos(angulo),0],[0,0,1]]))
    img_new =np.zeros_like(Imagen)
    for ind_c in range(c):
        for ind_y in range(h):
            for ind_x in range(w):
                v= np.matmul(np.array([ind_y,ind_x,1]),mat_inv)
                y_idx = v[0]
                x_idx = v[1]
                img_new[ind_y,ind_x,ind_c]=Imagen[int(y_idx)%h,int(x_idx)%w,ind_c]
    
    return img_new
    


imagen = plt.imread('SP.jpg')

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Original')
plt.axis('off')

imagen_ajustada = rotarImagen(imagen, 45)

# Mostrar la imagen con brillo ajustado
plt.subplot(1, 2, 2)
plt.imshow(imagen_ajustada)
plt.title('Rotacion ajustada')
plt.axis('off')

plt.show()
