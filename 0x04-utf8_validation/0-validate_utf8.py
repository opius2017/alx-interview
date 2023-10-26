#!/usr/bin/python3
"""Module for validUtf8 method"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    for num in data:
        # Mask to check if the most significant bit is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6

        if n_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            while num & mask1:
                n_bytes += 1
                mask1 = mask1 >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the current byte is a continuation byte
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0