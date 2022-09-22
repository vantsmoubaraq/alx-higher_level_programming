#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    le = len(argv)
    a = argv[1]
    b = argv[3]

    if(le < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    if(argv[2] == '+'):
        print("{:s} + {:s} = {:d}".format(a, b, add(int(a), int(b))))
    elif(argv[2] == '-'):
        print("{:s} - {:s} = {:d}".format(a, b, sub(int(a), int(b))))
    elif(argv[2] == "*"):
        print("{:s} * {:s} = {:d}".format(a, b, mul(int(a), int(b))))
    elif(argv[2] == '/'):
        print("{:s} / {:s} = {:d}".format(a, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
