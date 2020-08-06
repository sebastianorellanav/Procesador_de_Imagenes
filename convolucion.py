#Importar Librerías
import numpy as np

#Funciones

#Función que permite agregar un borde de ceros a una imagen (agranda el tamaño de la imagen)
#según un tamaño de borde ingresado
#Entrada: matriz de pixeles, entero, entero, entero 
#Salida: matriz de pixeles
def agregarBordesCeros(imagen, width, height,borde):
    nueva = np.zeros((height+(2 * borde), width+(2 * borde)))
    for i1,i2 in zip(range(borde,height+borde),range(0,height)):
        for j1,j2 in zip(range(borde,width+borde),range(0,width)):
            nueva[i1][j1] = imagen[i2][j2]

    return nueva

#Función que realiza la convolución entre una imagen y un kernel específico y reorna la imagen
# filtrada. El kernel y la imagen ingresada pueden ser de distintos tamaños (NxM)
#Entrada: matriz de pixeles, matriz 
#Salida: matriz de pixeles
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

