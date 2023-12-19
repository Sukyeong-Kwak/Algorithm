import sys
sys.setrecursionlimit(10**8)


def recur(y, x):
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        ey = y + dy
        ex = x + dx
        
        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)
        
    return dp[y][x]
        
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(n)]

# 모든 점을 방문한다

# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다

# 재귀로 구현한 뒤 DP로 바꾼다

point = 0

for y in range(n):
    for x in range(n):
        recur(y,x)

print(max(map(max, dp)) + 2) 