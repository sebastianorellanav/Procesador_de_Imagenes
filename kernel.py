#Importar Librerías
import numpy as np

#Funciones

#Funcion que crea un kernel de prueba para comprobar si el código de la convolución funciona correctamente.
#Esta comprobación se realiza en el Test 1.
#Entrada: -
#Salida: matriz 
def crearKernelTest():
    print("Generando kernel de prueba...")
    kernel = np.array([[256,256,256],
                        [256,256,256],
                        [256,256,256]])
    return kernel

#Función que crea un kernel gaussiano para implementar el filtro de suavizado.
#Entrada: -
#Salida: matriz
def crearKernelGaussiano():
    # Gaussian kernel
    print("Generando kernel gaussiano...")
    kernel = np.array([[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]])
    
    return kernel

#Función que crea un kernel para implementar el filtro detector de bordes.
#Entrada: -
#Salida: matriz
def crearKernelBordes():
    #kernel detector de bordes
    print("Generando kernel de bordes...")
    kernel = np.array(
              [[1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1]]
              )
    
    return kernel