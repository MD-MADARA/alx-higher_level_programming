#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo_l = my_list[:]
    for i in range(len(boo_l)):
        boo_l[i] = True if boo_l[i] % 2 == 0 else False
    return boo_l
