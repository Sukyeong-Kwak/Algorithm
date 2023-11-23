def recur(t):
    if (t == M):
        print(*arr)
        return
    
    for i in range(N):
        if numbers[i] in arr:
            continue
        arr.append(numbers[i])
        recur(t+1)
        arr.pop()
    

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []

recur(0)