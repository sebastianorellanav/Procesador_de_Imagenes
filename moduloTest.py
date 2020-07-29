#--------------------------------------------------------------------------------------------------------#
#Importar Librerias
import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion
import fourier as fourier

#--------------------------------------------------------------------------------------------------------#
#Test
#Test1: Se comprueba que la convolución con el filtro gaussiano funciona correctamente
def Test1():
    print("Test1")
    #Leer Imagen
    nombre = "lena512.bmp"
    imagen = lecturaEscritura.leerImagen(nombre)

    #Suavizado Gaussiano
    kernelGaussiano = kernel.crearKernelGaussiano()
    convolucionGaussiano = convolucion.aplicarConvolucion(imagen,kernelGaussiano)

    #Guardar Imagen
    lecturaEscritura.escribirImagen(convolucionGaussiano,"Convolucion filtro suavizado Gaussiano")
    
    return 1

#Test 2: Se comprueba que la convolución con el filtro de bordes funciona correctamente
def Test2():
    print("Test2")
    #Leer Imagen
    nombre = "lena512.bmp"
    imagen = lecturaEscritura.leerImagen(nombre)    

    #Detector de bordes
    kernelBordes = kernel.crearKernelBordes()
    convolucionBorde = convolucion.aplicarConvolucion(imagen,kernelBordes)

    #Guardar Imagen
    lecturaEscritura.escribirImagen(convolucionBorde,"Convolucion filtro detector de bordes")

    return 1

