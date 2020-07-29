from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

def leerImagen(nombre):
    print("Leyendo imagen...")
    imagen = imread(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')
    return imagen

def escribirImagen(imagen,nombre):
    print("Escribiendo imagen...")
    plt.figure()
    plt.title(nombre)
    plt.imshow(imagen, interpolation='nearest', cmap='gray')