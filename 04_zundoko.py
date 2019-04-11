import random

zundoko = ['zun', 'doko']
array = []
while(True):
    c = random.choice(zundoko)
    print(c)
    array.append(c)
    
    if len(array) >= 5:
        if ''.join(array[-6:-1]) == 'zunzunzunzundoko':
            print(''.join(array[-6:-1]))
            print ('KI・YO・SHI')
            break
        if len(array) >= 6:
            del array[0]
