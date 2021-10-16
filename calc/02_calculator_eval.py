import sys
import re


def main():
    argv = sys.argv
    first = str(argv[1])
    second = str(argv[2])
    operator = str(argv[3])
    print(eval(first + operator + second))

main()
