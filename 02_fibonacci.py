# Fibonacci数列
# 学ぶポイント
# 1. 繰り返し文(While)の扱い方
# 2. 数字リテラルの扱い方
# 3. 数字リテラつの足し算のやり方
first, second = 0, 1

while(first <= 10000):
    print(first)
    first, second = second, (first + second)