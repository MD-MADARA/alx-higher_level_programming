#!/usr/bin/python3
def handle_tuple(tup=()):
    if len(tup) == 0:
        return (0, 0)
    elif len(tup) == 1:
        return (tup[0], 0)

    return (tup[0], tup[1])


def add_tuple(tuple_a=(), tuple_b=()):
    a = handle_tuple(tuple_a)
    b = handle_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])
