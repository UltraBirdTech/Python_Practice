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
        print('[USAGE]:   python calculator.py [1つ目の数値][2つ目の数値][演算子(+-*/)]')
        print('[EXAMPLE]: python calculator.py 2 2 + ')
        exit()
    except NotMatchIntArgvError as err:
        print('[ERROR]: 計算する値は数値を入力してください。')
        num = str(err.num)
        value = err.value
        print('[ERROR]: 第' + num + '引数が数値に変換できない値"' + value + '"でした。')
        exit()
    except NotIncludeError as err:
        print('[ERROR]: 演算子が期待したものではありません。+, -, *, / のうちの一つからお選びください。')
        print('[ERROR]: "' + str(err) + '" is not include a list.')
        exit()
    except ZeroDivisionError as err:
        print('[ERROR]: 割り算を行う際に0徐算が発生しました。第2引数を1以上の数値にしてください。')
        print('[ERROR]: ' + str(err))
        exit()

    print(result)


def check_validate(argv):
    if len(argv) < 4:
        raise NotMatchArgvError()

    first = argv[1]
    if not str.isdigit(first):
        raise NotMatchIntArgvError(1, first)

    second = argv[2]
    if not str.isdigit(second):
        raise NotMatchIntArgvError(2, second)

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


class NotMatchIntArgvError(Exception):
    def __init__(self, num, value=''):
        self.num = num
        self.value = value

main()
