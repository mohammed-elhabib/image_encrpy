import secrets

import PIL
import numpy
import helper_method_enc
from helper_method_image import bainryToBlock, read_image, to_binary, block_to_binary, write_image
import time

start = time.time()
block_size = 4

img, width = read_image('8888.PNG', block_size)
blocks = bainryToBlock(img, block_size)
PRIME_RANGE_STOP = 1000

PRIME_RANGE_START = 500
p =  547#helper_method_enc.generate_p(PRIME_RANGE_START, PRIME_RANGE_STOP)
print(f"p : {p} ")
q =541#  helper_method_enc.generate_q(PRIME_RANGE_START, p)
print(f"q : {q} ")
n =295927# helper_method_enc.generate_n(p, q)
print(f"p : {n} ")

r = 983# helper_method_enc.gen_r(p, q, PRIME_RANGE_STOP)
print(f"r : {r} ")

k =  secrets.SystemRandom().randrange(17, 20)  # K>m
print(f"k : {k} ")

privateKey = k
publicKey = k + r * p

enc_m = [helper_method_enc.encrypt(c, publicKey, n) for c in blocks]
bin_enx = to_binary(enc_m)
size_enc = len(bin_enx)
print(size_enc)
image_enc=write_image(bin_enx,width)
image_out_enc = PIL.Image.fromarray(numpy.asarray(image_enc).astype('uint8'))
img_as_img_enc = image_out_enc.convert("RGB")
print(img_as_img_enc.size)
img_as_img_enc.show()

print(f"enc m size {size_enc} bit")
chars = [helper_method_enc.decrypt(c, privateKey, p) for c in enc_m]
block_bin = block_to_binary(chars, block_size)
print(f"enc  size / img size = {size_enc / len(block_bin)} ")

array_img = write_image(block_bin, width)

done = time.time()
elapsed = done - start
print(f"execution  time = {elapsed}  s")
image_out = PIL.Image.fromarray(numpy.asarray(array_img).astype('uint8'))
img_as_img = image_out.convert("RGB")
print(img_as_img.size)
img_as_img.show()
