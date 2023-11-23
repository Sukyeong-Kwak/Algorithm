import sys

N, H = map(int, sys.stdin.readline().split())

emos = [0 for _ in range(H+1)]

for i in range(N):
    h = int(sys.stdin.readline())
    if (i%2 == 0):
        emos[0] += 1
        emos[h] -= 1
    else:
        emos[H-h] += 1
        emos[H] -= 1

for i in range(1, H):
    emos[i] = emos[i-1] + emos[i]

min_value = min(emos[:-1])

print(min_value, emos.count(min_value))