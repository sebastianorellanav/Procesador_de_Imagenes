import numpy as np

def crearKernelGaussiano():
    # Gaussian kernel
    kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]
    
    return kernel

def crearKernelBordes():
    #kernel detector de bordes
    kernel = [[1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1],
              [1, 2, 0, -2, -1]]
    
    return kernel