#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    keys = list(a_dictionary)
    big_value = a_dictionary[keys[0]]
    big_key = keys[0]
    for key in keys:
        if a_dictionary[key] > big_value:
            big_value = a_dictionary[key]
            big_key = key
    return big_key
