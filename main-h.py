import os

import PIL.Image
import sympy  # pip install sympy
import secrets

from sympy import isprime

import lib

import csv

# from line_profiler import LineProfiler

# profile = LineProfiler()
from main import readimage, bainryToBlock, block_to_binary, block_to_decimal, writeimage, write_image

img, size = readimage('C:\\Users\\AURES\Downloads\\218715180_1699607756878227_1182138034353084512_n(1).jpg')
print(size)
PRIME_RANGE_STOP =int('1'*(size[0]*8*3)+'1',2)
PRIME_RANGE_START =int('1'*(size[0]*8*3),2)

p = lib.gen_p(PRIME_RANGE_START, PRIME_RANGE_STOP)


q = lib.gen_q(PRIME_RANGE_START, PRIME_RANGE_STOP, p)
n = lib.gen_n(p, q)
r = 15  # lib.gen_r(p,q, PRIME_RANGE_STOP)
k = secrets.SystemRandom().randrange(int('1'*(size[0]*8*3),2), int('1'*(size[0]*8*3)+'1',2))  # K>m
privateKey = k
publicKey = k + r * p
print('privateKey: '+ str(privateKey))
print('publicKey: '+ str(publicKey))

blocks = bainryToBlock(img,400)

# generate random message length 10
# print(f'Random msg: {msg}')
# encryption
enc_m = [lib.encrypt(block, publicKey, n) for block in blocks]
# decryption
chars = [lib.decrypt(c, privateKey, p) for c in enc_m]
last_block = block_to_decimal(chars,400,(size[0]*8*3))
blocks_dec= block_to_binary(last_block, 400, ((size[0] * 8 * 3) - 400))
#msg_d = ''.join(map(lambda x: chr(x), chars))
#print(f'decrypted msg: {msg}')
img = write_image(blocks_dec)
imge_out = PIL.Image.fromarray(img.astype('uint8'))
img_as_img = imge_out.convert("RGB")

img_as_img.show()