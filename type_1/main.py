import secrets

import PIL
import numpy
import helper_method_enc
from helper_method_image import bainryToBlock, read_image, to_binary, block_to_binary, write_image
import time

block_size = 50

############# read image and convert to bits ########################
start_read_image = time.time()
img, width = read_image('222.jpg', block_size)
blocks = bainryToBlock(img, block_size)
done_read_image = time.time()
elapsed_read_image = done_read_image - start_read_image
print(f"read image and convert to bits = {elapsed_read_image}s")

############### generate keys ############################
start_generate_keys = time.time()

PRIME_RANGE_STOP = 300_000_000_000_000_000

PRIME_RANGE_START = 100_000_000_000_000_000  # 500
p = helper_method_enc.generate_p(PRIME_RANGE_START, PRIME_RANGE_STOP)  # 547  #
print(f"p : {p} ")
q = helper_method_enc.generate_q(PRIME_RANGE_START, p)  # 541  #
print(f"q : {q} ")
n = helper_method_enc.generate_n(p, q)  # 295927
print(f"p : {n} ")

r = helper_method_enc.gen_r(p, q, PRIME_RANGE_STOP)  # 983
print(f"r : {r} ")

k = secrets.SystemRandom().randrange(int('1' * block_size, 2) + 1, int('1' * block_size, 2) + 100)  # K>m
print(f"k : {k} ")

privateKey = k
publicKey = k + r * p
done_generate_keys = time.time()
elapsed_generate_keys = done_generate_keys - start_generate_keys
print(f"generate keys time = {elapsed_generate_keys}s")
############## enc image bits ################
start_enc = time.time()
enc_m = [helper_method_enc.encrypt(c, publicKey, n) for c in blocks]
done_enc = time.time()
elapsed_enc = done_enc - start_enc
print(f"enc  time = {elapsed_enc}  s")

############## show enc image  ################
start_show_enc = time.time()
bin_enx = to_binary(enc_m)
size_enc = len(bin_enx)
image_enc = write_image(bin_enx, width)
image_out_enc = PIL.Image.fromarray(numpy.asarray(image_enc).astype('uint8'))
img_as_img_enc = image_out_enc.convert("RGB")
img_as_img_enc.show()

done_show_enc = time.time()
elapsed_show_enc = done_show_enc - start_show_enc
print(f" convert enc  bits to image and show time  = {elapsed_show_enc}s")
################ dec image


start_dec = time.time()
chars = [helper_method_enc.decrypt(c, privateKey, p) for c in enc_m]
done_dec = time.time()
elapsed_dec = done_dec - start_dec
print(f"dec  time = {elapsed_dec} s")

########### shwo original image #################
start_show_original_image = time.time()

block_bin = block_to_binary(chars, block_size)
print(f"enc  size / img size = {size_enc / len(block_bin)} ")

array_img = write_image(block_bin, width)

image_out = PIL.Image.fromarray(numpy.asarray(array_img).astype('uint8'))
img_as_img = image_out.convert("RGB")
img_as_img.show()
done_show_original_image = time.time()
elapsed_show_original_image = done_show_original_image - start_show_original_image
print(f"show original image  time = {elapsed_show_original_image} s")
print(f"Total  execution time = {done_show_original_image - start_read_image} s")
