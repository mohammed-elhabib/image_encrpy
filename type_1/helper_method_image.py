import secrets

import PIL.Image
import numpy
from PIL import Image

from numpy import array

import helper_method_enc


def read_image(path, block_size):
    fin = Image.open(path)
    print(fin.size)
    image = array(fin)
    # width = bin(fin.size[0])[2:]
    # div_width = block_size - len(width)
    # if (div_width > 0):
    #   width = '0' * div_width + width
    image_bits = []
    for row in range(fin.size[1]):
        for i_pixel in range(fin.size[0]):
            pixel = image[row][i_pixel]
            for i_rgb in range(3):
                rgb_s = bin(pixel[i_rgb])[2:]
                if (len(rgb_s) < 8):
                    zero_number = 8 - len(rgb_s)
                    rgb_s = '0' * zero_number + rgb_s
                image_bits.append( rgb_s)
    return ''.join([rgb for rgb in image_bits]), fin.size[0]


def write_image(array_image, width):

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
    return ''.join([block_to_bin(block, block_size) for block in blocks])


def block_to_bin(block, block_size):
    block_bin = bin(block)[2:]
    if len(block_bin) < block_size:
        block_bin = '0' * (block_size - len(block_bin)) + block_bin
    return block_bin


def to_binary(blocks: []):
    return ''.join([bin(block)[2:] for block in blocks])
