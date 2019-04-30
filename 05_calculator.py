# calculator.py
# 学ぶポイント
# 1. 引数の扱い方
# 2. 条件分岐のポイント
# 3. 数値リテラルの四則演算
# 4. エラーチェック(try, except)
import sys

operators = ('+', '-', '*', '/')

def main():
    # recieve args.
    args = sys.argv

    try:
        first, second, operator= check_validate(args)
        calculate(first, second, operator)
    except ZeroDivisionError as err:
        print('[ERROR]: 割り算を行う際に0徐算が発生しました。第二引数を1以上の数値にしてください。')
        print('[ERROR]: ', str(err))
        exit()
    except ValueError as err:
        print('[ERROR]: 計算する値は数値を入力してください。')
        print('[ERROR]: ', str(err))
        exit()
    except NotIncludeError as err:
        print('[ERROR]: 演算子が期待したものではありません。+-*/のうちの一つからお選びください')
        print('[ERROR]: ', str(err), 'is not include a list')
        exit()
    except NotMatchArgvError as err:
        print('[ERROR]:   引数の数が足りません')
        print('[USAGE]:   python 05_calculator.py [最初の数値][2つ目の数値][演算子(+-*/)]')
        print('[EXAMPLE]: python 05_calculator.py 2 2 + ')
        exit()


def check_validate(args):
    # check args num
    if len(args) < 4:
        raise NotMatchArgvError()

    first = int(args[1])
    second = int(args[2])
    operator = args[3]
    
    # check operator
    if not operator in operators:
        raise NotIncludeError(operator)

    return first, second, operator

def calculate(first, second, operator):
    ans = 0
    if operator == '+':
        ans = first + second

    elif operator == '-':
        ans = first - second

    elif operator == '*':
        ans = first * second

    elif operator == '/':
        ans = first / second

    else:
        print('[ERROR]: 演算子が期待したものではありません。+-*/のうちの一つからお選びください')
        exit()

    print(ans)

class NotIncludeError(Exception):
    pass

class NotMatchArgvError(Exception):
    pass

main()
