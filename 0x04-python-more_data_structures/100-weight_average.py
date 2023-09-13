#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    s_score = 0   # f_score = sum of score * weight
    s_weight = 0  # s_weight = sum of weights
    for tup in my_list:
        s_score += tup[0] * tup[1]
        s_weight += tup[1]
    return s_score / s_weight
