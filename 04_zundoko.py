import random

zundoko = ['ズン', 'ドコ']
array = []
while(True):
    array.append(random.choice(zundoko))
    print(array[-1])
    if len(array) >= 5:
        str = ''.join(array)
        if str == 'ズンズンズンズンドコ':
            print(str)
            print('KI・YO・SHI')
            break

        del array[0]
