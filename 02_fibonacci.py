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
