import random

zundoko = ('ズン', 'ドコ')
zundoko_array = []
while(True):
    zundoko_array.append(random.choice(zundoko))
    print(zundoko_array[-1])
    if len(zundoko_array) >= 5:
        s = ''.join(zundoko_array)
        if s == 'ズンズンズンズンドコ':
            print(s)
            print('KI・YO・SHI')
            break

        del zundoko_array[0]
