##########calculator.py############################
# 学ぶポイント
# 1. 引数の扱い方
# 2. 条件分岐のポイント
# 3. 数値リテラルの四則演算
###################################################

import sys

# recieve args.
args = sys.argv

# check args
if len(args) < 4:
    print('[ERROR]:   引数の数が足りません')
    print('[USAGE]:   python 05_calculator.py [最初の数値]、[二つ目の数値]、[計算方法(+-*/)]')
    print('[EXAMPLE]: python 05_calculator.py 2 2 + ')
    exit()

first = int(args[1])
second = int(args[2])
operator = args[3]

ans = 0

if operator == '+':
    ans = first + second

elif operator == '-':
    ans = first - second

elif operator == '*':
    ans = first * second

elif operator == '/':
    # check zero
    if second == 0:
        print('[ERROR]: second is 0')
        exit()
    ans = first /second

else:
    print('[ERROR]: 演算子が期待したものではありません。+-*/のうちの一つからお選びください')
    exit()
    
print(ans)
