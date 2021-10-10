import sys
import re

argv = sys.argv
first = int(argv[1])
second = int(argv[2])
operator = argv[3]

if operator == '+':
    print(first + second)

elif operator == '-':
    print(first - second)

elif operator == '*':
    print(first * second)

elif operator == '/':
    print(first / second)
else:
    print('計算できませんでした')
