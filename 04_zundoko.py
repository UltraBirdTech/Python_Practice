import random

zundoko = ('ズン', 'ドコ')
array = []
while(True):
    array.append(random.choice(zundoko))
    print(array[-1])
    if len(array) >= 5:
        s = ''.join(array)
        if s == 'ズンズンズンズンドコ':
            print(s)
            print('KI・YO・SHI')
            break

        del array[0]
