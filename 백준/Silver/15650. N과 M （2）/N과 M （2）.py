def recur(number):
    if (number == M):
        print(*arr)
        return
    
    for i in range(1, N+1):
        if len(arr) > 0 and i <= arr[-1]:
            continue
        arr.append(i)
        recur(number+1)
        arr.pop()
    

N, M = map(int, input().split())
arr = []

recur(0)