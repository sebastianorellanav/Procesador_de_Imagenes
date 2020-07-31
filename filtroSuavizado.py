import kernel as kernel
import convolucion as convolucion

def filtroSuavizado(imagen):
    #Suavizado Gaussiano
    kernelGaussiano = kernel.crearKernelGaussiano()
    convolucionGaussiano = convolucion.aplicarConvolucion(imagen,kernelGaussiano)

    return convolucionGaussiano