for i in range(1,100):
    string = ''
    if (i % 3) == 0:
        string = string + 'fizz'
    if (i % 5) == 0:
        string = string + 'buzz'

    if string != '':
        print(str(i) + ':' + string)
