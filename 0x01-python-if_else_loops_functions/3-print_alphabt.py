#!/usr/bin/python3
for character in range(26):
    if chr(character + 97) != 'e' and chr(character + 97) != 'q':
        print("{:c}".format(character + 97), end="")
