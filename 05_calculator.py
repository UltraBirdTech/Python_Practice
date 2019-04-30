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
    argv = sys.argv

    try:
        check_validate(argv)
        calculate(int(argv[1]), int(argv[2]), argv[3])
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


def check_validate(argv):
    # check argv num
    if len(argv) < 4:
        raise NotMatchArgvError()

    first = int(argv[1])
    second = int(argv[2])
    operator = argv[3]
    
    # check operator
    if not operator in operators:
        raise NotIncludeError(operator)

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
