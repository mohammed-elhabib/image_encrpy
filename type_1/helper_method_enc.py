import sympy
import secrets


def generate_p(range_start, range_stop):
    return sympy.randprime(range_start, range_stop)


def generate_q(range_start, p):
    while True:
        q = sympy.randprime(range_start, p)
        if q < p:
            break

    return q


def generate_n(p, q):
    return p * q


def gen_r(q,prime_range_start, prime_range_stop):
    secrets_gen = secrets.SystemRandom()

    while True:
        r = secrets_gen.randrange(prime_range_start, prime_range_stop)

        if r > q:
            break
    return r

def fragment(m: int):
    size_of_int_m = len(str(m))
    if size_of_int_m == 1:
        return {'part_1': 0, 'part_2': m}
    exp = 2
    #if size_of_int_m > 2:
     #   rn = secrets.SystemRandom()
      #  exp = rn.randrange(1, size_of_int_m)
    m2 = m % (10 ** exp)
    m1 = m - m2
    return {'part_1': m1, 'part_2': m2}


def encrypt(message, public_key, n):
    parts = fragment(message)
    part_1 = parts['part_1']
    part_2 = parts['part_2']
    return (part_1 + public_key * part_2) % n


def decrypt(c, private_key, p):
    return (c % p) % (private_key - 1)


