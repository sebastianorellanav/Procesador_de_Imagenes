import numpy as np

def agregarBordesCeros(imagen, width, height,borde):
    nueva = np.zeros((height+1, width+1))
    for i1,i2 in zip(range(1,height + 1),range(0,height)):
        for j1,j2 in zip(range(1,width+1),range(0,width)):
            nueva[i1][j1] = imagen[i2][j2]
    
    return nueva

def suavisado(imagen, width, height):
    # Gaussian kernel
    kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
              [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
              [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]

    # Select kernel here:
    kernel = box_kernel

    # Middle of the kernel
    offset = len(kernel) // 2

    # Create output image
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)

    # Compute convolution between intensity and kernels
    for x in range(offset, input_image.width - offset):
        for y in range(offset, input_image.height - offset):
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[a][b]
                    acc[1] += pixel[1] * kernel[a][b]
                    acc[2] += pixel[2] * kernel[a][b]

            draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
        
    output_image.save("output.png")
