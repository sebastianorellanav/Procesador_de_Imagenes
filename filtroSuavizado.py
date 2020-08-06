#Importar Librerías
import kernel as kernel
import convolucion as convolucion

#Funciones

#Esta función implementa un filtro de suavizado. Primero se crea el kernel gaussiano y luego
#se aplica la convolución entre el kernel y la imagen ingresada.
#Entrada: matriz de pixeles
#Salida: matriz de pixeles
def filtroSuavizado(imagen):
    #Suavizado Gaussiano
    kernelGaussiano = kernel.crearKernelGaussiano()
    convolucionGaussiano = convolucion.aplicarConvolucion(imagen,kernelGaussiano)

    return convolucionGaussiano