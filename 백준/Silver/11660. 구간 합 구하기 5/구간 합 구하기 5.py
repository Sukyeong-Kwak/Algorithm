import sys

N, M = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적합 table 만들기
prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for x in range(N):
    for y in range(N):
        prefix[x+1][y+1] = table[x][y] + prefix[x][y+1] + prefix[x+1][y] - prefix[x][y]

# 답 구하기 
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])