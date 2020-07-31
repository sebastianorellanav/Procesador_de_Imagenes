import numpy as np

def crearKernelTest():
    print("Generando kernel de prueba...")
    kernel = np.array([[256,256,256],
                        [256,256,256],
                        [256,256,256]])
    return kernel

def crearKernelGaussiano():
    # Gaussian kernel
    print("Generando kernel gaussiano...")
    kernel = np.array([[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]])
    
    return kernel

def crearKernelBordes():
    #kernel detector de bordes
    print("Generando kernel de bordes...")
    kernel = np.array(
              [[1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1]]
              )
    
    return kernel