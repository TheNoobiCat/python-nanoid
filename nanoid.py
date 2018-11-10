# coding: utf-8

from __future__ import unicode_literals
from __future__ import division

import math
import random
from os import urandom


def generate(alphabet='_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
             size=21, secure=True):
    if secure:
        return _generate_secure(alphabet, size)
    else:
        return _generate_non_secure(alphabet, size)


def _generate_secure(alphabet, size):
    """
    Create a nanoid
    :param alphabet: optional, specify the alphabets for Nano ID generation
    :param size: optional, specify the size of the Nano ID
    :return: Nano ID string
    """
    if not alphabet:
        return ''
    if size < 1:
        return ''
    masks = [15, 31, 63, 127, 255]
    mask = 1
    for m in masks:
        if m >= len(alphabet) - 1:
            mask = m
            break
    step = int(math.ceil(1.6 * mask * size / len(alphabet)))
    nano_id = ''
    while True:
        random_bytes = bytearray(urandom(step))
        for i in range(step):
            rand_byte = random_bytes[i] & mask
            if rand_byte < len(alphabet):
                if alphabet[rand_byte]:
                    nano_id += alphabet[rand_byte]
                    if len(nano_id) >= size:
                        return nano_id


def _generate_non_secure(alphabet, size):
    nano_id = ''
    for i in range(size):
        nano_id += random.choice(alphabet)
    return nano_id


if __name__ == '__main__':
    print(generate())
