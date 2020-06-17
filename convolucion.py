import numpy as np

def agregarBordesCeros(imagen, width, height,borde):
    nueva = np.zeros((height+(2 * borde), width+(2 * borde)))
    for i1,i2 in zip(range(borde,height+borde),range(0,height)):
        for j1,j2 in zip(range(borde,width+borde),range(0,width)):
            nueva[i1][j1] = imagen[i2][j2]
    
    return nueva

def convolucion(imagen, width, height, kernel):
    # Mitad del Kernel
    borde = len(kernel) // 2

    imagen = agregarBordesCeros(imagen,width,height,borde)

    # Crear imagen de Salida
    nueva = np.zeros(len(imagen))

    # Compute convolution between intensity and kernels
    for x in range(borde, width - borde):
        for y in range(borde, height - borde):
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - borde
                    yn = y + b - borde
                    pixel = imagen[xn, yn] * kernel[a][b]


