import numpy
from PIL import Image

from numpy import array


def readimage(path):
    fin = Image.open(path)
    # converting image into byte array to perform decryption easily on numeric data
    image = array(fin)
    #   PIL.Image.fromarray(image, "RGB").show()

    image_bits = []
    for col in image:
        col_s = ''
        for pix in col:
            pix_s = ''
            for rgb in pix:
                rgb_s = bin(rgb)[2:]
                if (len(rgb_s) < 8):
                    zeroo_number = 8 - len(rgb_s)
                    rgb_s = '0' * zeroo_number + rgb_s
                pix_s += rgb_s
            col_s += pix_s
        image_bits.append(col_s)

    return image_bits, fin.size
    # performing XOR operation on each value of bytearray


def write_image(array_image):
    image = []
    for col_s in array_image:
        pix = []
        for i_pix in range(int(int(len(col_s)) / 24)):
            pix_s = col_s[i_pix * 24:i_pix * 24 + 24]
            rgb = []
            for i_rgbs in range(3):
                rgb.append(int(pix_s[i_rgbs * 8:i_rgbs * 8 + 8], 2))
            pix.append(rgb)
        image.append(pix)
    return numpy.asarray(image)


def bainryToBlock(array_binary: [], len_m1):
    blocks = []
    for pixel in array_binary:
        blocks.append([int(pixel[0:len_m1], 2), int(pixel[len_m1:], 2)])
    return blocks


def block_to_decimal(block_decimal: [], len_m1, size):
    binaries = []
    for pixel in block_decimal:
        binary = bin(pixel)[2:]
        div = size - len(binary)
        if div>0:
            binary = '0' * div + binary
        binaries.append([int(binary[0:len_m1], 2), int(binary[len_m1:], 2)])
    return binaries


def block_to_binary(blocks: [], len_m1, len_m2):
    blocks_St = []
    for block in blocks:
        m1 = bin(block[0])[2:]
        m2 = bin(block[1])[2:]
        if len(m1) < len_m1:
            m1 = '0' * (len_m1 - len(m1)) + m1
        div_m2 = len_m2 - len(m2)
        if div_m2 > 0:
            m2 = '0' * div_m2 + m2
        blocks_St.append(m1 + m2)
    return blocks_St
print(int('1'*1000,2))
# bainary = block_to_bainary(blocks,400,20232-400)
# img2 = writeimage(bainary)

# imge_out = Image.fromarray(img2.astype('uint8'))
# img_as_img = imge_out.convert("RGB")

# img_as_img.show()
