import numpy as np

def agregarBordesCeros(imagen, width, height,borde):
    nueva = np.zeros((height+(2 * borde), width+(2 * borde)))
    for i1,i2 in zip(range(borde,height+borde),range(0,height)):
        for j1,j2 in zip(range(borde,width+borde),range(0,width)):
            nueva[i1][j1] = imagen[i2][j2]

    return nueva

def aplicarConvolucion(imagen,kernel):
    print("Aplicando convolución...")
    [h, w] = imagen.shape
    [p, q] = kernel.shape
    borde = len(kernel) // 2
   
    imagenConMargen = agregarBordesCeros(imagen,w,h,borde)
    [h, w] = imagenConMargen.shape
    # Crear imagen de Salida
    nueva =  np.array([])

    # Compute convolution between intensity and kernels
    for x in range(borde, h - borde):
        for y in range(borde, w - borde):
            pixel = 0
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - borde
                    yn = y + b - borde
                    pixel += imagenConMargen[xn, yn] * kernel[a][b]
                   
            nueva = np.append(nueva,pixel)
                   
    #Ajustando a dimensiones originales
    nueva = np.reshape(nueva,imagen.shape)
    return nueva

