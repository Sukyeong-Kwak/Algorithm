import sys

n = int(input())
inputs = [sys.stdin.readline() for _ in range(n)]

result = []

for input in inputs:
    command = input.split()[0]
    # print(command, result)
    if command == 'push':
        result.append(input.split()[1])
    elif command == 'pop':
        if len(result) == 0:print(-1)
        else: print(result.pop())
    elif command == 'size':
        print(len(result))
    elif command == 'empty':
        print(int(len(result) == 0))
    elif command == 'top':
        if len(result) == 0: print(-1)
        else: print(result[-1])
    
    