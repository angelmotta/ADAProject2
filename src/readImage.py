import numpy as np
from PIL import Image

'''
Source:
https://note.nkmk.me/en/python-numpy-opencv-image-binarization/
https://www.prasannakumarr.in/journal/color-to-grayscale-python-image-processing
'''


def readImage(fileImage, umbral):
    im = np.array(Image.open(fileImage).convert('L').resize((256, 256)))
    print(im)
    im_bool = im > umbral
    print(im_bool)
    # Convert to black and white
    im_bin_128 = (im > umbral) * 255
    print(im_bin_128)
    Image.fromarray(np.uint8(im_bin_128)).save('img/lena_square_blackandwhite.jpg')
    # Return matrix  0s and 1s
    im_bin_01 = (im > umbral) * 1
    print(im_bin_01)
    return im_bin_01


readImage('img/lena_square.jpg', 128)
