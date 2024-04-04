#!/usr/bin/python3
"""
Module 0-validate_utf8
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        mask = 10000000
        while mask & byte:
            num_bytes += 1
            mask >>= 1

        if num_bytes == 0:
            continue
        if num_bytes == 1 or num_bytes > 4:
            return False

        num_bytes -= 1

    return num_bytes == 0
