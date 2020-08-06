#Importar Librerías
import numpy as np

#Funciones

#Función que aplica la transformada de fourier a una señal en 2 dimensiones (imagen)
#Entrada: matriz de pixeles
#Salida: matriz 
def transformadaFourier(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)                 #Moviendo bajas frecuencias al centro
    valorTransformada = np.log(np.abs(fshift))
    return valorTransformada