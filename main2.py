import secrets

import numpy
from PIL import Image

from numpy import array

import lib


def read_image(path, block_size):
    fin = Image.open(path)
    # converting image into byte array to perform decryption easily on numeric data
    image = array(fin)
    print(fin)
    #   PIL.Image.fromarray(image, "RGB").show()
    width = bin(fin.size[0])[2:]
    div_width = block_size - len(width)
    if (div_width > 0):
        width = '0' * div_width + width
    image_bits = width
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
        image_bits += col_s

    return image_bits, fin.size[0]
    # performing XOR operation on each value of bytearray


def write_image(array_image, block_size):
    width_str = array_image[:block_size]
    array_image = array_image[block_size:]
    width = int(width_str, 2)
    print(width)
    image = []
    row_num = int(len(array_image) / (width * 24))
    print(row_num)
    index_pixel = 0
    for row in range(row_num):
        pixel = []
        for i_pixel in range(width):
            pixel_str = array_image[index_pixel * 24:index_pixel * 24 + 24]
            rgb = []
            for i_rgb in range(3):
                rgb.append(int(pixel_str[i_rgb * 8:i_rgb * 8 + 8], 2))
            pixel.append(rgb)
            index_pixel += 1
        image.append(pixel)
    return numpy.asarray(image)


def bainryToBlock(binary_str: [], block_size, len_m1):
    blocks = []
    num_blocks = int(len(binary_str) / block_size)
    for i_block in range(num_blocks):
        block_str = binary_str[i_block * block_size:i_block * block_size + block_size]
        blocks.append([int(block_str[0:len_m1], 2), int(block_str[len_m1:], 2)])
    return blocks


def block_to_decimal(block_decimal: [], len_m1, size):
    binaries = []
    for pixel in block_decimal:
        binary = bin(pixel)[2:]
        div = size - len(binary)
        if div > 0:
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


img, size = read_image('C:\\Users\\AURES\Downloads\\218715180_1699607756878227_1182138034353084512_n.jpg', 1000)
# res = write_image(img, 1000)

blocks = bainryToBlock(img, 1000, 400)
print(blocks[-1])
print("///")
PRIME_RANGE_STOP = int('1' * 1000 + '1', 2)
PRIME_RANGE_START = int('1' * 1000, 2)

p = lib.gen_p(PRIME_RANGE_START, PRIME_RANGE_STOP)
q = lib.gen_q(PRIME_RANGE_START, PRIME_RANGE_STOP, p)
n = lib.gen_n(p, q)
r = lib.gen_r( q,PRIME_RANGE_START, PRIME_RANGE_STOP)
k = secrets.SystemRandom().randrange(int('1' * 1000, 2), int('1' * 1000 + '1', 2))  # K>m
privateKey = k
publicKey = k + r * p
print('privateKey: ' + str(privateKey))
print('publicKey: ' + str(publicKey))
enc_m = [lib.encrypt(block, publicKey, n) for block in blocks]
dec_m = [lib.decrypt(c, privateKey, p) for c in enc_m]
print(block_to_decimal(dec_m,400,1000)[-1])
# print(int('1' * 1000, 2))
# bainary = block_to_bainary(blocks,400,20232-400)
# img2 = writeimage(bainary)

# imge_out = Image.fromarray(res.astype('uint8'))
# img_as_img = imge_out.convert("RGB")

# img_as_img.show()
