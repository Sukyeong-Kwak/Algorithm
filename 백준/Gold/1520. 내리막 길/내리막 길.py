import sys
sys.setrecursionlimit(10**8)

def recur(y, x):
    
    if y == h-1 and x == w-1:
        return 1
        
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        ey = y + dy
        ex = x + dx
        
        if 0 <= ey < h and 0 <= ex < w:
            if graph[y][x] > graph[ey][ex]:
                route += recur(ey, ex)
    
    dp[y][x] = route
    return dp[y][x]
                
        
h, w = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(h)]

dp = [[-1 for _ in range(w)] for _ in range(h)]

print(recur(0,0))

