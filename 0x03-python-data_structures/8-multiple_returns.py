#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    fc = None if length == 0 else sentence[0]
    return (length, fc)
