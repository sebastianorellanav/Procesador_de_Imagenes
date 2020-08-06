##########################################################################################################
###########################   Laboratorio 2: Procesador de Imágenes     ##################################
###########################         Sebastian Orellana Verdejo          ##################################
###########################            Franco Tapia Cabañas             ##################################
###########################                                             ##################################
###########################            Redes de Computadores            ##################################
##########################################################################################################
###########################    Nota: La ejecución del programa dura     ##################################
###########################          3 minutos aprox.                   ##################################
##########################################################################################################

#Importar Librerias
import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion
import fourier as fourier
import filtroSuavizado as fs
import filtroDetectorBordes as fdb

#---------------------------------------------------------------------------------------------------------#
#Main
nombre = "lena512.bmp"
imagen = lecturaEscritura.leerImagen(nombre)

#Suavizado Gaussiano
convolucionGaussiano = fs.filtroSuavizado(imagen)

#Detector de bordes
convolucionBorde = fdb.filtroDetectorBordes(imagen)

#Transformada de fourier
fourierOriginal = fourier.transformadaFourier(imagen)
fourierGaussiano = fourier.transformadaFourier(convolucionGaussiano)
fourierBorde = fourier.transformadaFourier(convolucionBorde)

#Guardando resultados
lecturaEscritura.escribirImagen(convolucionGaussiano,"Convolucion filtro suavizado Gaussiano")
lecturaEscritura.escribirImagen(convolucionBorde,"Convolucion filtro detector de bordes")
lecturaEscritura.escribirImagen(fourierOriginal,"Transformada original")
lecturaEscritura.escribirImagen(fourierGaussiano,"Transformada suavizado Gaussiano")
lecturaEscritura.escribirImagen(fourierBorde,"Transformada detector de bordes")
plt.show()


  