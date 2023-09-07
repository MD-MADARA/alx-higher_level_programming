#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as av

    ac = len(av)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(av[1])
    b = int(av[3])
    op = av[2]
    if op == '+':
        result = add(a, b)

    elif op == '-':
        result = sub(a, b)

    elif op == '*':
        result = mul(a, b)

    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, result))
