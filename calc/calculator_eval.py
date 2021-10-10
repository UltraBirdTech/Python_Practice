# calculator.py
# 学ぶポイント
# 1. 引数の扱い方
# 2. 条件分岐のポイント
# 3. 数値リテラルの四則演算
# 4. エラーチェック(try, except)
import sys
import re


def main():
    argv = sys.argv
    first = str(argv[1])
    second = str(argv[2])
    operator = str(argv[3])
    print(eval(first + operator + second))

main()
