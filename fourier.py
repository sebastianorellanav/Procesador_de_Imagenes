import numpy as np

def transformadaFourier(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)                 #Moviendo bajas frecuencias al centro
    valorTransformada = np.log(np.abs(fshift))
    return valorTransformada