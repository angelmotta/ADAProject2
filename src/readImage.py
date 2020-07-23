import numpy as np
from PIL import Image
from intersect import isInside, Point
from memoizedv2 import getMemorizedTrapezes
'''
Source:
https://note.nkmk.me/en/python-numpy-opencv-image-binarization/
https://www.prasannakumarr.in/journal/color-to-grayscale-python-image-processing
'''


def readImage(fileImage, umbral):
    im = np.array(Image.open(fileImage).convert('L').resize((256, 256)))
    #print(im)
    im_bool = im > umbral
    #print(im_bool)
    # Convert to black and white
    im_bin_128 = (im > umbral) * 255
    #print(im_bin_128)
    #Image.fromarray(np.uint8(im_bin_128)).save('img/lena_square_blackandwhite.jpg')
    # Return matrix  0s and 1s
    im_bin_01 = (im > umbral) * 1
    #print(im_bin_01)
    return im_bin_01


def main():
    # Numero de imagenes intermedias
    t = 10
    
    img_in = readImage('img/lena_square.jpg', 128)
    img = Image.fromarray(np.uint8(img_in*255))
    img.save('images/t_0.png')
    img_out = readImage('img/image_bw.jpg', 128)
    img = Image.fromarray(np.uint8(img_out*255))
    img.save('images/t_' + str(t+1) + '.png')
    print('[ - ] Imagenes cargadas')
    for i in range(1, t + 1):
        f_t = []
        print('[ - ] Imagen Transitoria ' + str(i))
        for j, r_in in enumerate(img_in):
            r_out = img_out[j]
            #p,w = minMatchMemorized(r_in, r_out)
            
            # Polygons almacenara los trapecios bajo la siguiente estructura
            # [ [Point(x1, 0), Point(x2, 0), Point(x3, t + 1), Point(x4, t + 1)], [...], ... ]
            # - Los 2 primeros puntos corresponderian a el techo del trapecio
            # - Los 2 ultimos a la base
            # - En el poligono, 2 puntos consecutivos deben estar unidos por una linea, caso contrario se generaria un error
            polygons = getMemorizedTrapezes(r_in, r_out, t)
            print('[ - ] Min Match - Fila ' + str(j) + ' de ' + str(len(img_in)))
            r_t = []
            for k, c_in in enumerate(r_in):
                intersect = False
                for polygon in polygons:
                    if isInside(polygon, Point(k, i)):
                        intersect = True
                        break
                if intersect:
                    r_t.append(255)
                else:
                    r_t.append(0)
            f_t.append(r_t)
        img = Image.fromarray(np.uint8(f_t))
        img.save('images/t_' + str(i) + '.png')
        print('[ * ] Imagen creada ' + str(i))
        f_t.clear()

main()