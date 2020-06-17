from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

def leerImagen(nombre):
    imagen = imread(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')
    plt.show()
    return imagen

def escribirImagen(imagen,nombre):
    plt.title(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')
    plt.show()