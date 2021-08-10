from array import array

from PIL.Image import Image


def read_image(path):
    fin = Image.open(path)
    print(fin.size)
    image = array(fin)
    width = bin(fin.size[0])[2:]
    for row in image:
        for col in row:
            for pixel in col:
                print(pixel)
