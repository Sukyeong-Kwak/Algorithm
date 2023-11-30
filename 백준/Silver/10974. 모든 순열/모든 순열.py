import sys
sys.setrecursionlimit(10**6)

def recur(number):
    global arr, answer, flag
    
    if number == N:
        print(*arr)
        return
            
    
    for i in range(1, N+1):
        if i in arr: continue
        arr.append(i)
        recur(number+1)
        arr.pop()

N = int(input())
arr = []

recur(0)