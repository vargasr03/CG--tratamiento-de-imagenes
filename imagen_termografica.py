# Valentina Vargas - Juan Chaux


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ImagenTiff=np.array(plt.imread("FLIR_00088.tiff"))
D=np.double(ImagenTiff)
Min=-40
Max=160
Bits=14
MatrizC=np.array((Max-Min)*D/2**Bits+Min) 

fig=plt.figure("Imagen termografica")
plt.imshow(MatrizC, cmap=plt.cm.hot_r)
CooMax=np.argwhere(MatrizC==np.max(MatrizC))[0]
CooMin=np.argwhere(MatrizC==np.min(MatrizC))[0]
print(f"Coordenada Maxima:{tuple(CooMax)}")
print(f"Coordenada Minima:{tuple(CooMin)}")
plt.plot(CooMax[1],CooMax[0],'wo')
plt.plot(CooMin[1],CooMin[0],'bd')                 
plt.colorbar(shrink=.92)   
plt.figure("Histograma")
hist, bins =np.histogram(MatrizC, np.arange(0,Max), density=True)                                                                               
HistoTempeBar=np.int32(MatrizC.round())
plt.hist(HistoTempeBar, 5, facecolor='red', alpha=0.5) 
print(f"Promedio:{np.mean(MatrizC)}")
print(f"Mediana:{np.median(MatrizC)}")
print(f"Moda:{np.argmax(MatrizC)}")
print(f"Maximo:{np.max(MatrizC)}")
print(f"Minimo:{np.min(MatrizC)}")

plt.show()



