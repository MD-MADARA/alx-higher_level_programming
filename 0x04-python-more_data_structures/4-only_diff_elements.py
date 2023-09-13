#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    d1 = set_1 - set_2
    d2 = set_2 - set_1
    return d1 | d2
