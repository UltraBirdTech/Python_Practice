
array = []
def fibo(n):
    array.append(n)
    print(array)
    if (n==0):
        return 0

    elif (n == 1):
        return 1

    print(n)
    return fibo(n - 1) + fibo(n -2)

for i in range(10):
    print('==========' +str(i) + '===========')
    print('result:' + str(fibo(i)))

