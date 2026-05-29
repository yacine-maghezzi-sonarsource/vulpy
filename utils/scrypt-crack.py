#!/usr/bin/env python3

import sys
import os
import binascii
from binascii import unhexlify

import click

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

@click.command()
@click.argument('key')
@click.argument('salt')
def crack_scrypt(key, salt):

    try:
        salt_bytes = unhexlify(salt.encode())
        key_bytes = unhexlify(key.encode())
    except binascii.Error:
        print('Non-hexadecimal data on salt and/or key', file=sys.stderr)
        return False

    backend = default_backend()

    for number in range(10000):

        kdf = Scrypt(
            salt=salt_bytes,
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=backend
        )

        try:
            kdf.verify(str(number).encode(), key_bytes)
            print('Cracked! Password:', number)
            break
        except InvalidKey:
            pass


if __name__ == '__main__':
    crack_scrypt()

