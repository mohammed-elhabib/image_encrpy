import secrets

import PIL.Image
import numpy
from PIL import Image

from numpy import array

import lib

def read_image(path, block_size):
    fin = Image.open(path)
    print(fin.size)
    image = array(fin)
    width = bin(fin.size[0])[2:]
    div_width = block_size - len(width)
    if (div_width > 0):
        width = '0' * div_width + width
    image_bits = width
    for row in range(fin.size[1]):
        for i_pixel in range(fin.size[0]):
            pixel = image[row][i_pixel]
            pix_s = ''
            for i_rgb in range(3):
                rgb_s = bin(pixel[i_rgb])[2:]
                if (len(rgb_s) < 8):
                    zeroo_number = 8 - len(rgb_s)
                    rgb_s = '0' * zeroo_number + rgb_s
                pix_s += rgb_s
            image_bits += pix_s
    print(len(image_bits))
    return image_bits


def write_image(array_image, block_size):

    width_str = array_image[:block_size]
    array_image = array_image[block_size:]

    width = int(width_str, 2)
    image = []

    row_num = int(len(array_image) / (width * 24))

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


def bainryToBlock(binary_str: [], block_size):
    blocks = []

    num_blocks = int(len(binary_str) / block_size)
    for i_block in range(num_blocks):
        block_str = binary_str[i_block * block_size:i_block * block_size + block_size]
        blocks.append(int(block_str, 2))
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


def block_to_binary(blocks: [], block_size):
    blocks_St = ''
    for block in blocks:
        block_bin = bin(block)[2:]
        if len(block_bin) < block_size:
            block_bin = '0' * (block_size - len(block_bin)) + block_bin
        blocks_St += block_bin
    print(len(blocks_St))
    return blocks_St


img = read_image('C:\\Users\\PC\\Pictures\\Saved Pictures\\image.png', 16)
# res = write_image(img, 1000)

blocks = bainryToBlock(img, 16)
PRIME_RANGE_STOP = 999_999_999_9
PRIME_RANGE_START = 100_000_000_0

p = lib.gen_p(PRIME_RANGE_START, PRIME_RANGE_STOP)
q = lib.gen_q(PRIME_RANGE_START, p)
n = lib.gen_n(p, q)
r = lib.gen_r(p, q, PRIME_RANGE_STOP)
k = secrets.SystemRandom().randrange(50000, 80000)  # K>m

privateKey = k
publicKey = k + r * p

# generate random message length 10
msg = blocks
# encryption
enc_m = [lib.encrypt(c, publicKey, n) for c in msg]
# decryption
chars = [lib.decrypt(c, privateKey, p) for c in enc_m]
block_bin = block_to_binary(chars, 16)
array_img = write_image(block_bin, 16)
# print(int('1' * 1000, 2))
# bainary = block_to_bainary(blocks,400,20232-400)
# img2 = writeimage(bainary)

imge_out = Image.fromarray(numpy.array(array_img).astype('uint8'))
img_as_img = imge_out.convert("RGB")
print(img_as_img.size)
img_as_img.show()
