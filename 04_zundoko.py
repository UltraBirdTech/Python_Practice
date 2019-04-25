import random

zundoko = ['zun', 'doko']
array = []
while(True):
    array.append(random.choice(zundoko))
    print(array[-1])
    if len(array) >= 5:
        str = ''.join(array)
        if str == 'zunzunzunzundoko':
            print(str)
            print('KI・YO・SHI')
            break

        del array[0]
