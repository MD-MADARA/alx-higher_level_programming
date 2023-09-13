#!/usr/bin/python3

def search_replace(my_list, search, replace):

    return list(map(lambda e: e if e != search else replace, my_list))
