#--------------------------------------------------------------------------------------------------------#
#Importar Librerias
import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion
import fourier as fourier
import filtroSuavizado as fs
import filtroDetectorBordes as fdb

#--------------------------------------------------------------------------------------------------------#
#Test1: Función que comprueba si el algortimo de convolución implementado funciona correctamente
#Entrada: void
#Salida: entero
def Test1():
    print("Test 1")
    #Leer Imagen
    nombre = "lena512.bmp"
    imagen = lecturaEscritura.leerImagen(nombre)
    
    #Aplicar convolucion entre el kernel y la imagen
    Kernel = kernel.crearKernelTest()
    result = convolucion.aplicarConvolucion(imagen, Kernel)

    return 1


#Test2: Se comprueba que la convolución con el filtro gaussiano funciona correctamente
#Entrada: void
#Salida: entero
def Test2():
    print("Test 2")
    #Leer Imagen
    nombre = "lena512.bmp"
    imagen = lecturaEscritura.leerImagen(nombre)

    #Suavizado Gaussiano
    result = fs.filtroSuavizado(imagen)

    return 1

#Test 3: Se comprueba que la convolución con el filtro de bordes funciona correctamente
#Entrada: void
#Salida: entero
def Test3():
    print("Test 3")
    #Leer Imagen
    nombre = "lena512.bmp"
    imagen = lecturaEscritura.leerImagen(nombre)    

    #Detector de bordes
    result = fdb.filtroDetectorBordes(imagen)

    return 1

