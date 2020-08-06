#Importar Librerías
import kernel as kernel
import convolucion as convolucion

#Funciones

#Función que implementa un filtro detector de bordes. Primero se crea el kernel para detectar bordes
#y luego se aplica la convolución entre el mismo kernel y la imagen ingresda.
#Entrada: matriz de pixeles
#Salida: matriz de pixeles
def filtroDetectorBordes(imagen):
    #Detector de bordes
    kernelBordes = kernel.crearKernelBordes()
    convolucionBorde = convolucion.aplicarConvolucion(imagen,kernelBordes)

    return convolucionBorde