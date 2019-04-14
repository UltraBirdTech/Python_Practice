#######Fibonacci数列#####################
# 学ぶポイント
# 1. 繰り返し文(While)の扱い方
# 2. 数字リテラルの扱い方
# 3. 数字リテラつの足し算のやり方
#########################################

# CONST VERBS
FIRST_ELEMENT = 0
SECOND_ELEMENT = 1
LIMIT = 10000

# verbs
first = FIRST_ELEMENT
second = SECOND_ELEMENT
temp = 0

while(first <= LIMIT):
    print(first)
    temp = first + second
    first = second
    second = temp
