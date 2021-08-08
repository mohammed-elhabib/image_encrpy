import profile
import random
import string

import sympy  # pip install sympy
import secrets
import math


def gen_p(range_start, range_stop):
    return sympy.randprime(range_start, range_stop)


def gen_q(range_start, p):
    print(range_start,p)
    while True:
        q = sympy.randprime(range_start, p)
        if q < p:
            break

    return q


def gen_n(p, q):
    return p * q


def gen_r(q,prime_range_start, prime_range_stop):

    while True:
        secrets_gen = secrets.SystemRandom()
        r = secrets_gen.randrange(prime_range_start, prime_range_stop)

        if r > q:
            break
    return r


# def str_num_rep(msg):
#     return int.from_bytes(msg.encode('utf-8'), 'big')

# def str_num_rep(msg):
#     return int.from_bytes(msg.encode("ascii", "ignore"), 'big')

def str_num_rep(msg):
    return list(msg.encode("ascii", "ignore"))


def int_str_rep(i, length):
    return i.to_bytes(length, 'big').decode()


def fragment_msg(m: int):
    size_of_int_m = len(str(m))
    if size_of_int_m == 1:
        return {'m1': 0, 'm2': m}
    exp = 1
    if size_of_int_m > 2:
        rn = secrets.SystemRandom()
        exp = rn.randrange(1, size_of_int_m)  # number of digits for m2 starting from the least significant digit
    m2 = m % (10 ** exp)
    m1 = m - m2
    return {'m1': m1, 'm2': m2}


def encrypt(m: int, public_key: int, n: int):
    parts = fragment_msg(m)
    m1 = parts['m1']
    m2 = parts['m2']
    return (m1 + public_key * m2) % n


def decrypt(c, private_key, p):
    return (c % p) % (private_key - 1)


sympy.ntheory.totient


def rand_msg(length: int) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
