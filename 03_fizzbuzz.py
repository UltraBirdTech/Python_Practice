# fizzbuzz
# 学ぶポイント
# 1. 条件分岐(if)
# 2. 文字列リテラルの扱い方
# 3. 数字リテラルの余剰の出し方

FIZZ = 'fizz'
BUZZ = 'buzz'

for i in range(1, 100):
    s = ''
    if (i % 3) == 0:
        s += FIZZ
    if (i % 5) == 0:
        s += BUZZ

    if s != '':
        print(str(i) + ':' + s)
