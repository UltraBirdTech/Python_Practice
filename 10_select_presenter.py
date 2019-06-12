import random

LineNum = 10
members = ['M1', 'M2', 'M3']
i = 1

while len(members) != 0:
    presenter = random.choice(members)

    string = ''
    if type(presenter) == str:
        string += presenter + 'さん'
    else:
        for p in presenter:
            string += p + 'さん'
        
    print(str(i) + '番目に発表する人は' + str(string) + 'です。' + ('\n' * LineNum))
        
    members.remove(presenter)
    print('残りの発表者数は' + str(len(members)) + '組です。')
    i += 1
    input()
