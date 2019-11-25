import random

LineNum = 10
members = ['M1', 'M2', 'M3']

while len(members):
    presenter = random.choice(members)

    string = ''
    if type(presenter) == str:
        string += presenter + 'さん'
    else:
        for p in presenter:
            string += p + 'さん'

    print('次に発表する人は' + str(string) + 'です。' + ('\n' * LineNum))
        
    members.remove(presenter)
    print('残りの発表者数は' + str(len(members)) + '組です。')
    input()
