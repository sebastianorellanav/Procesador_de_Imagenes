#Importar Librerías
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

#Funciones

#Función que lee una imagen desde un archivo específico, el cuál se ingresa como parámetro. 
#Entrada: String
#Salida: matriz de pixeles
def leerImagen(nombre):
    print("Leyendo imagen...")
    imagen = imread(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')
    return imagen

#Función que guarda una matriz de pixeles como un archivo png con nombre ingresado como parámetro
#Entrada: matriz de pixeles, String
#Salida: void
def escribirImagen(imagen,nombre):
    print("Escribiendo imagen...")
    plt.figure()
    plt.title(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')