import numpy as np

def crearKernelGaussiano():
    # Gaussian kernel
    kernel = np.array(
              [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]
              )
    
    return kernel

def crearKernelBordes():
    #kernel detector de bordes
    kernel = np.array(
              [[1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1]]
              )
    
    return kernel

def crearKernelLaplaciano():
    #kernel laplaciano
    kernel = np.array(
             [[0, 1, 0],
             [1,-4, 1],
             [0, 1, 0]]
             )
    return kernel
