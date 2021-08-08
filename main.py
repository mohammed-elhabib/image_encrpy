import secrets

import PIL
import sympy
import numpy
import helper_method_enc
from helper_method_image import bainryToBlock, read_image, to_binary, block_to_binary, write_image
import time

start = time.time()
block_size = 16

img = read_image('8888.PNG', block_size)
blocks = bainryToBlock(img, block_size)
PRIME_RANGE_STOP = 999_999_999_9
PRIME_RANGE_START = 100_000_000_0

p = helper_method_enc.generate_p(PRIME_RANGE_START, PRIME_RANGE_STOP)
q = helper_method_enc.generate_q(PRIME_RANGE_START, p)
n = helper_method_enc.generate_n(p, q)
r = helper_method_enc.gen_r(p, q, PRIME_RANGE_STOP)
k = secrets.SystemRandom().randrange(50000, 80000)  # K>m

privateKey = k
publicKey = k + r * p

enc_m = [helper_method_enc.encrypt(c, publicKey, n) for c in blocks]

size_enc = len(to_binary(enc_m))
print(f"enc m size {size_enc} bit")
chars = [helper_method_enc.decrypt(c, privateKey, p) for c in enc_m]
block_bin = block_to_binary(chars, block_size)
print(f"enc  size / img size = {size_enc / len(block_bin)} ")

array_img = write_image(block_bin, block_size)

done = time.time()
elapsed = done - start
print(f"execution  time = {elapsed}  s")
image_out = PIL.Image.fromarray(numpy.asarray(array_img).astype('uint8'))
img_as_img = image_out.convert("RGB")
print(img_as_img.size)
img_as_img.show()
