def recur(t):
    if (t == M):
        print(*arr)
        return
    
    for i in range(N):
        if len(arr) > 0 and numbers[i] < arr[-1]:
            continue
        arr.append(numbers[i])
        recur(t+1)
        arr.pop()
    

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []

recur(0)