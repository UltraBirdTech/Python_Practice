# calculator.py
# 学ぶポイント
# 1. 引数の扱い方
# 2. 条件分岐のポイント
# 3. 数値リテラルの四則演算
# 4. エラーチェック(try, except)
import sys

operators = ('+', '-', '*', '/')


def main():
    argv = sys.argv
    result = 0

    try:
        check_validate(argv)
        result = calculate(int(argv[1]), int(argv[2]), argv[3])
    except NotMatchArgvError as err:
        print('[ERROR]:   引数の数が足りません。')
        print('[USAGE]:   python calculator.py [最初の数値][2つ目の数値][演算子(+-*/)]')
        print('[EXAMPLE]: python calculator.py 2 2 + ')
    except ValueError as err:
        print('[ERROR]: 計算する値は数値を入力してください。')
        print('[ERROR]: ', str(err))
    except NotIncludeError as err:
        print('[ERROR]: 演算子が期待したものではありません。+, -, *, / のうちの一つからお選びください。')
        print('[ERROR]: "', str(err), '" is not include a list.')
    except ZeroDivisionError as err:
        print('[ERROR]: 割り算を行う際に0徐算が発生しました。第2引数を1以上の数値にしてください。')
        print('[ERROR]: ', str(err))
    finally:
        exit()

    print(result)


def check_validate(argv):
    if len(argv) < 4:
        raise NotMatchArgvError()

    operator = argv[3]
    if operator not in operators:
        raise NotIncludeError(operator)


def calculate(first, second, operator):
    if operator == '+':
        return first + second

    elif operator == '-':
        return first - second

    elif operator == '*':
        return first * second

    elif operator == '/':
        return first / second

    else:
        # 事前に演算子チェックをしているため、ここには到達しない
        raise NotIncludeError(operator)


class NotIncludeError(Exception):
    pass


class NotMatchArgvError(Exception):
    pass

main()
