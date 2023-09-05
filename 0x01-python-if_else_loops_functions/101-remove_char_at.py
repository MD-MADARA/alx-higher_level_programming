#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        cpy = str
    else:
        cpy = str[:n] + str[n + 1:]
    return cpy
