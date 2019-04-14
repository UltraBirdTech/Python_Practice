import sys

# recieve args.
args = sys.argv
first = int(args[1])
second = int(args[2])
operator = args[3]

ans = 0

if operator == '+':
    ans = first + second

elif operator == '-':
    ans = first - second

elif operator == '*':
    ans = first * second

elif operator == '/':
    # check zero
    if second == 0:
        print('[ERROR]: second is 0')
        exit()
    ans = first /second
    
print(ans)
