import numpy as numpy
import matplotlib.pyplot as plt
import lecturaEscritura as lecturaEscritura
import kernel as kernel
import convolucion as convolucion

nombre = "lena512.bmp"
imagen = lecturaEscritura.leerImagen(nombre)
kernel = kernel.crearKernel1()
convolucion = convolucion.aplicarConvolucion(imagen,kernel)

print(convolucion)
lecturaEscritura.escribirImagen(convolucion)



  