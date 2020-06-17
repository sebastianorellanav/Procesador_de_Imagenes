import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion
import fourier as fourier

nombre = "lena512.bmp"
imagen = lecturaEscritura.leerImagen(nombre)

#Suavizado Gaussiano
kernelGaussiano = kernel.crearKernelGaussiano()
convolucionGaussiano = convolucion.aplicarConvolucion(imagen,kernelGaussiano)

#Detector de bordes
kernelBordes = kernel.crearKernelBordes()
convolucionBorde = convolucion.aplicarConvolucion(imagen,kernelBordes)

#Transformada de fourier
fourier = fourier.transformadaFourier(imagen)
fourierGaussiano = fourier.transformadaFourier(convolucionGaussiano)
fourierBorde = fourier.transformadaFourier(convolucionBorde)

#Guardando resultados
lecturaEscritura.escribirImagen(convolucionGaussiano)
lecturaEscritura.escribirImagen(convolucionBorde)
lecturaEscritura.escribirImagen(fourier)
lecturaEscritura.escribirImagen(fourierGaussiano)
lecturaEscritura.escribirImagen(fourierGausfourierBordesiano)


  