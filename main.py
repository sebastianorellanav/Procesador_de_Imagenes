import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion
import fourier as fourier

nombre = "lena512.bmp"
imagen = lecturaEscritura.leerImagen(nombre)

#Kernels de prueba
kernelLaplaciano = kernel.crearKernelLaplaciano()
convolucionLaplaciano = convolucion.aplicarConvolucion(imagen,kernelLaplaciano)

#Suavizado Gaussiano
kernelGaussiano = kernel.crearKernelGaussiano()
convolucionGaussiano = convolucion.aplicarConvolucion(imagen,kernelGaussiano)

#Detector de bordes
kernelBordes = kernel.crearKernelBordes()
convolucionBorde = convolucion.aplicarConvolucion(imagen,kernelBordes)

#Transformada de fourier kernel prueba
fourierLaplaciano = fourier.transformadaFourier(convolucionLaplaciano)

#Transformada de fourier
fourierOriginal = fourier.transformadaFourier(imagen)
fourierGaussiano = fourier.transformadaFourier(convolucionGaussiano)
fourierBorde = fourier.transformadaFourier(convolucionBorde)

#Guardando resultados
lecturaEscritura.escribirImagen(convolucionGaussiano,"Convolucion filtro suavizado Gaussiano")
lecturaEscritura.escribirImagen(convolucionBorde,"Convolucion filtro detector de bordes")
lecturaEscritura.escribirImagen(convolucionLaplaciano,"Convolución Laplaciano")

lecturaEscritura.escribirImagen(fourierOriginal,"Transformada original")
lecturaEscritura.escribirImagen(fourierGaussiano,"Transformada suavizado Gaussiano")
lecturaEscritura.escribirImagen(fourierBorde,"Transformada detector de bordes")
lecturaEscritura.escribirImagen(fourierLaplaciano,"Transformada laplaciano")


  