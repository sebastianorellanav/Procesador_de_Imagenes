import kernel as kernel
import convolucion as convolucion

def filtroDetectorBordes(imagen):
    #Detector de bordes
    kernelBordes = kernel.crearKernelBordes()
    convolucionBorde = convolucion.aplicarConvolucion(imagen,kernelBordes)

    return convolucionBorde