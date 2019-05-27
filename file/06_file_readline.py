with open('10.txt', 'rt') as f:
    # read()
    print(f.read())

    # readline()
    for i in range(1,10):
       print(f.readline(), end='')

    # 繰り返し
    for data in f:
        print(data, end='')