#######fizzbuzz##########################
# 学ぶポイント
# 1. 条件分岐(if)
# 2. 文字列リテラルの扱い方
# 3. 数字リテラルの余剰の出し方
#########################################

for i in range(1,100):
    string = ''
    if (i % 3) == 0:
        string += 'fizz'
    if (i % 5) == 0:
        string += 'buzz'

    if string != '':
        print(str(i) + ':' + string)
